import os
import json

root_dir = r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki\Raw\Sources"
large_files = []

for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith(".md"):
            full_path = os.path.join(dirpath, f)
            size = os.path.getsize(full_path)
            if size > 46080:
                large_files.append({"file": full_path, "size": size})

out_path = r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki\scripts\large_files.json"
with open(out_path, "w", encoding="utf-8") as out:
    json.dump(large_files, out, indent=2)

print(f"Found {len(large_files)} large files. Details saved to scripts/large_files.json")
