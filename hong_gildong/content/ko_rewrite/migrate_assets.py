import json, hashlib, os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = __file__.rsplit("\\", 1)[0]
CONTENT = HERE.rsplit("\\", 1)[0]
MODULE = CONTENT.rsplit("\\", 1)[0]
dest = os.path.join(MODULE, "src", "main", "assets", "books")
os.makedirs(dest, exist_ok=True)
manifest = {
    "source": "hong_gildong/content (36장 완판본, 공유마당, 자유이용 만료)",
    "generated_by": "content/ko_rewrite/migrate_assets.py from content/chapter_NN_draft.json",
    "files": {},
}
for n in range(1, 13):
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
