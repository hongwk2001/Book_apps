import json

subagents = []
for i in range(1, 57):
    input_file = f"c:\\git_repo\\Book_apps\\secret_garden\\batches\\batch_{i}.json"
    output_file = f"c:\\git_repo\\Book_apps\\secret_garden\\batches\\batch_{i}_done.json"
    
    subagents.append({
        "TypeName": "TranslationChunker",
        "Role": f"Chunker {i}",
        "Prompt": f"Read input file: {input_file}\nWrite output to: {output_file}\nProcess all paragraphs and report when done.",
        "Model": "flash"
    })

with open("c:\\git_repo\\Book_apps\\secret_garden\\subagent_payload.json", "w") as f:
    json.dump(subagents, f, indent=2)
