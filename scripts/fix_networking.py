import os
import re

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"Raw\Sources\Learn Networking In 25 MINUTES Crash Course  Networking Fundamentals + Cloud Networking Concepts.md")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r"^title:", "Title:", content, flags=re.MULTILINE)
content = re.sub(r"^created:", "Created:", content, flags=re.MULTILINE)
if "Processed: true" not in content:
    content = content.replace("tags:", "Processed: true\nReference: \"[[Networking Fundamentals Crash Course]]\"\ntags:")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Networking file frontmatter fixed.")
