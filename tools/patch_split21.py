with open(r'C:\git_repo\Book_apps\tools\execute_split_21.py', encoding='utf-8') as f:
    code = f.read()

bad_str = '"ko2": "몇 걸음 떨어진 곳에는 육중한 쇠창살이 가로질러 있는 작은 굴뚝이 있었고, 벽난로 안에는 부드럽고 오래된 나무 재가 한 무더기 쌓여 있었다."'
good_str = '"ko2": "몇 발자국 떨어진 곳에는 무거운 쇠창살이 가로질러진 작은 굴뚝이 있었고, 벽난로에는 부드럽고 오래된 나무 재 더미가 놓여 있었다."'

assert bad_str in code
code = code.replace(bad_str, good_str)

with open(r'C:\git_repo\Book_apps\tools\execute_split_21.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched execute_split_21.py successfully!")
