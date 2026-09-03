import json

with open('paras_over_300.txt', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the top 36 (400-499 chars)
from list_paras_over_300 import over_300, b_400_499

print(f"Total >= 400 chars: {len(b_400_499)}")
single_sents = [p for p in b_400_499 if p['sents'] == 1]
multi_sents = [p for p in b_400_499 if p['sents'] > 1]
print(f"  Single sentence: {len(single_sents)}")
print(f"  Multi sentence : {len(multi_sents)}")

print("\n--- SINGLE SENTENCE >= 400 CHARS ---")
for p in single_sents:
    print(f"{p['ch']} ID {p['id']} ({p['chars']} chars): {p['en'][:90]}...")

print("\n--- MULTI SENTENCE >= 400 CHARS ---")
for p in multi_sents:
    print(f"{p['ch']} ID {p['id']} ({p['chars']} chars, {p['sents']} sents): {p['en'][:90]}...")
