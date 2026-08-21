import os

base_dir = r'c:\git_repo\Book_apps\frankenstein\prep_data'

def fix_ch5():
    filepath = os.path.join(base_dir, '9.ch5_ko.txt')
    with open(filepath, 'r', encoding='utf-8') as f:
        paras = [p for p in f.read().split('\n\n') if p.strip()]
    
    # Merge para 7 and 8
    if '인적' in paras[8]:
        paras[7] = paras[7] + '\n' + paras[8]
        del paras[8]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(paras))
    print('Fixed 9.ch5_ko.txt')

def fix_ch7():
    filepath = os.path.join(base_dir, '11.ch7_ko.txt')
    with open(filepath, 'r', encoding='utf-8') as f:
        paras = [p for p in f.read().split('\n\n') if p.strip()]
    
    # Merge para 34 and 35
    if '빅터' in paras[35]:
        paras[34] = paras[34] + ' ' + paras[35]
        del paras[35]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(paras))
    print('Fixed 11.ch7_ko.txt')

fix_ch5()
fix_ch7()