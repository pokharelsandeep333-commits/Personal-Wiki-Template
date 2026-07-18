import os

folder = r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki\Raw\Sources\sandeepcloudserver"
files = os.listdir(folder)
for file in files:
    if not file.endswith(".md"): continue
    path = os.path.join(folder, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Reference:" not in content:
        # insert Reference before tags:
        content = content.replace("tags:\n  - \"source\"", "Reference: \"[[General]]\"\ntags:\n  - \"source\"")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added Reference to {file}")
