import os
import glob

base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "")
concepts_dir = os.path.join(base_dir, "Wiki", "Concepts")

count = 0
for filepath in glob.glob(os.path.join(concepts_dir, "*.md")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "example_source_folder/" in content:
        new_content = content.replace("example_source_folder/", "ExampleSourceFolder/")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
        count += 1
print(f"Total concept notes updated: {count}")
