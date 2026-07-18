import os

folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"Raw\Sources\example_source_folder")
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
