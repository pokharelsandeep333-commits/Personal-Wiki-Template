import os

folder = r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki\Raw\Sources\sandeepcloudserver"
files = os.listdir(folder)
for file in files:
    if not file.endswith(".md"): continue
    path = os.path.join(folder, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Processed: true" in content: continue
    
    frontmatter = f"""---
Title: "{file.replace('.md', '').replace('_', ' ')}"
ContentType:
  - "markdown"
Created: 2026-07-10
Processed: true
tags:
  - "source"
---
"""
    if not content.startswith("---"):
        with open(path, "w", encoding="utf-8") as f:
            f.write(frontmatter + content)
        print(f"Added frontmatter to {file}")
    else:
        print(f"Skipped {file} (already has frontmatter)")
