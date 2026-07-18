import os
import glob

base_dir = r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki"
concepts_dir = os.path.join(base_dir, "Wiki", "Concepts")

count = 0
for filepath in glob.glob(os.path.join(concepts_dir, "*.md")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "sandeepcloudserver/" in content:
        new_content = content.replace("sandeepcloudserver/", "SandeepCloudServer/")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
        count += 1
print(f"Total concept notes updated: {count}")
