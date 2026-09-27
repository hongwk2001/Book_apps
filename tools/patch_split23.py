with open(r'C:\git_repo\Book_apps\tools\execute_split_23.py', encoding='utf-8') as f:
    code = f.read()

bad_str = '"ko2": "“하늘과 정의, 관대함, 그리고 귀하의 고귀한 가문 이름의 명예를 걸고!” 불쌍한 죄수의 그 외침을 그는 자신이 사랑하는 모든 것을 뒤로 한 채 자석 바위를 향해 떠내려가며 약해지는 용기를 북돋우기 위해 반복했다."'
good_str = '"ko2": "하늘과 정의, 관대함, 그리고 귀하의 고귀한 가문 이름의 명예를 걸고! 불쌍한 죄수의 그 외침을 그는 자신이 사랑하는 모든 것을 뒤로 한 채 자석 바위를 향해 떠내려가며 약해지는 용기를 북돋우기 위해 반복했다."'

assert bad_str in code
code = code.replace(bad_str, good_str)

with open(r'C:\git_repo\Book_apps\tools\execute_split_23.py', 'w', encoding='utf-8') as f:
    f.write(code)
print("Updated execute_split_23.py successfully!")
