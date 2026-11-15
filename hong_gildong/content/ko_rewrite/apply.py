import json, sys, importlib
sys.stdout.reconfigure(encoding="utf-8")
HERE = __file__.rsplit("\\", 1)[0]
CONTENT = HERE.rsplit("\\", 1)[0]
sys.path.insert(0, HERE)

for arg in sys.argv[1:]:
    n = arg  # e.g. "03"
    KO = importlib.import_module(f"ch{n}").KO
    path = f"{CONTENT}\\chapter_{n}_draft.json"
    cards = json.load(open(path, encoding="utf-8"))
    miss = [c["tag"] for c in cards if c["tag"] not in KO and not c["is_header"] and c["tag"] != "P0001_src"]
    print(path.rsplit("\\", 1)[1], "missing:", miss)
    for c in cards:
        if c["tag"] in KO:
            c["ko"] = KO[c["tag"]]
    json.dump(cards, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("applied", sum(1 for c in cards if c["tag"] in KO))
