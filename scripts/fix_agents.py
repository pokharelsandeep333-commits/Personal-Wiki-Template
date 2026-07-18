import os

files = [
    (r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki\Raw\Sources\SandeepCloudServer\.agents\AGENTS.md", "SandeepCloud Agent Rules"),
    (r"C:\Users\DSU\OneDrive - Dakota State University\Obsidian Vault\LLM-Wiki\Raw\Sources\SandeepCloudServer\.agents\PROJECT_LOG.md", "SandeepCloud Project Log")
]

for path, title in files:
    if not os.path.exists(path): continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not content.startswith("---"):
        fm = f"""---
Title: "{title}"
Reference: "[[SandeepCloud Project Architecture]]"
ContentType:
  - "markdown"
Created: 2026-07-10
Processed: true
tags:
  - "source"
---
"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(fm + content)
        print(f"Added frontmatter to {os.path.basename(path)}")
