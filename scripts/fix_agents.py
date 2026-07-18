import os

files = [
    (os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"Raw\Sources\ExampleSourceFolder\.agents\AGENTS.md"), "ExampleProject Agent Rules"),
    (os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"Raw\Sources\ExampleSourceFolder\.agents\PROJECT_LOG.md"), "ExampleProject Project Log")
]

for path, title in files:
    if not os.path.exists(path): continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not content.startswith("---"):
        fm = f"""---
Title: "{title}"
Reference: "[[ExampleProject Project Architecture]]"
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
