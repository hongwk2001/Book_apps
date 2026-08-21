import json

calls = []
for i in range(1, 15):
    calls.append({
        "TypeName": "TranslationChunker",
        "Role": f"Chunker {i}",
        "Prompt": f"Read input file: c:\\git_repo\\Book_apps\\secret_garden\\batches\\batch_{i}.json\nWrite output to: c:\\git_repo\\Book_apps\\secret_garden\\batches\\batch_{i}_done.json\nProcess all paragraphs and report when done.",
        "Model": "flash"
    })

print(json.dumps(calls))
