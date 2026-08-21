import os
import shutil

sg_dir = r'c:\git_repo\Book_apps\secret_garden'
prep_dir = os.path.join(sg_dir, 'prep_data')
dracula_dir = r'c:\git_repo\Book_apps\dracula'

# 1. Reorganize Folder Structure
if not os.path.exists(prep_dir):
    os.makedirs(prep_dir)

# Move all existing files/folders in secret_garden to prep_data
for item in os.listdir(sg_dir):
    if item == 'prep_data':
        continue
    src_path = os.path.join(sg_dir, item)
    dst_path = os.path.join(prep_dir, item)
    shutil.move(src_path, dst_path)
    print(f"Moved {item} to prep_data")

# 2. Scaffold the App Module (Copy from dracula)
# Copy all contents of dracula into secret_garden
for item in os.listdir(dracula_dir):
    if item in ['build', '.cxx']: # Skip build folders if they exist
        continue
    src_path = os.path.join(dracula_dir, item)
    dst_path = os.path.join(sg_dir, item)
    
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    else:
        shutil.copy2(src_path, dst_path)
    print(f"Copied {item} from dracula to secret_garden")

