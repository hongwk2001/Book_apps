import json

def main():
    data = json.load(open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_27.ch23.json', encoding='utf-8'))
    with open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/temp_read.txt', 'w', encoding='utf-8') as f:
        for i, d in enumerate(data):
            f.write(f'--- ID {d["id"]} ---\n')
            f.write(f"EN: {d['en']}\n")
            f.write(f"KO: {d['ko']}\n\n")

if __name__ == '__main__':
    main()
