import os
import shutil

src_dir = r'c:\git_repo\Book_apps\secret_garden'
dst_dir = r'c:\git_repo\Book_apps\frankenstein'

# Copy everything except prep_data and build
for item in os.listdir(src_dir):
    if item in ['prep_data', 'build']:
        continue
    src_path = os.path.join(src_dir, item)
    dst_path = os.path.join(dst_dir, item)
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    else:
        shutil.copy2(src_path, dst_path)
print("Copied files to Frankenstein module")
