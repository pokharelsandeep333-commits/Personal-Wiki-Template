import os
import glob
import re

raw_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"Raw\Sources")
wiki_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Wiki")

# Find all markdown files in Raw/Sources
raw_files = []
for root, _, files in os.walk(raw_dir):
    for f in files:
        if f.endswith(".md"):
            raw_files.append(f)

# Find all wiki notes
wiki_notes = []
for root, _, files in os.walk(wiki_dir):
    for f in files:
        if f.endswith(".md"):
            wiki_notes.append(os.path.join(root, f))

# Extract all referenced sources from wiki notes
referenced_sources = set()
for note in wiki_notes:
    with open(note, "r", encoding="utf-8") as f:
        content = f.read()
        # Look for sources block in frontmatter
        sources_match = re.search(r'sources:\n(.*?)\n(?:[a-z_]+:|\-\-\-)', content, re.DOTALL)
        if sources_match:
            sources_block = sources_match.group(1)
            # Find all [[filename]]
            sources = re.findall(r'\[\[(.*?)\]\]', sources_block)
            for src in sources:
                basename = os.path.basename(src)
                if basename.endswith(".md"):
                    referenced_sources.add(basename)
                    referenced_sources.add(basename[:-3])
                else:
                    referenced_sources.add(basename)
                    referenced_sources.add(basename + ".md")

# Compare
uningested = []
for rf in raw_files:
    if rf not in referenced_sources and rf[:-3] not in referenced_sources:
        uningested.append(rf)

if uningested:
    print("WARNING: The following raw files are NOT referenced in any wiki note:")
    for uf in uningested:
        print(f"  - {uf}")
else:
    print("SUCCESS: All raw files are referenced in at least one wiki note.")
