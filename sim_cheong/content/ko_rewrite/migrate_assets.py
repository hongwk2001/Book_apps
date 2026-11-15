import json, hashlib, os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.dirname(HERE)
MODULE = os.path.dirname(CONTENT)
dest = os.path.join(MODULE, "src", "main", "assets", "books")
os.makedirs(dest, exist_ok=True)
N_CHAPTERS = 13
manifest = {
    "source": "sim_cheong/content (完板 71장본, 위키문헌, PD-old-100)",
    "generated_by": "content/ko_rewrite/migrate_assets.py from content/chapter_NN_draft.json",
    "files": {},
}
for n in range(1, N_CHAPTERS + 1):
    cards = json.load(open(os.path.join(CONTENT, f"chapter_{n:02d}_draft.json"), encoding="utf-8"))
    for i, c in enumerate(cards):
        c["id"] = i + 1
    data = (json.dumps(cards, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    name = f"ch_{n:02d}.json"
    open(os.path.join(dest, name), "wb").write(data)
    manifest["files"][name] = hashlib.sha256(data).hexdigest()
    print(name, len(cards))
open(os.path.join(dest, "_source.json"), "w", encoding="utf-8").write(
    json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")
print("manifest written")
