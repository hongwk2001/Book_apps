import os
import glob

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data\batches"
all_batches = set(os.path.basename(f).replace(".json", "") for f in glob.glob(os.path.join(base_dir, "batch_*.json")) if not f.endswith("_done.json"))
done_batches = set(os.path.basename(f).replace("_done.json", "") for f in glob.glob(os.path.join(base_dir, "batch_*_done.json")))

missing = all_batches - done_batches
print(f"Missing: {missing}")
