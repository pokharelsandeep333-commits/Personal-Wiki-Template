import os
import re

folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"Wiki\Concepts")
files_to_fix = [
    "Kubernetes Architecture.md",
    "Kubernetes Pods.md",
    "Kubernetes Deployments and ReplicaSets.md",
    "Semantic Search Vector Database Architecture.md",
    "Docker Base Image Security and OS Vulnerabilities.md",
    "Kubernetes Networking and Services.md",
    "Kubernetes Autoscaling.md"
]

for file in files_to_fix:
    path = os.path.join(folder, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace tag: "concept" with tags:\n  - "concept"
    content = content.replace('tag: "concept"', 'tags:\n  - "concept"')
    
    # Calculate source_count
    sources_match = re.search(r'sources:\n(.*?)updated:', content, re.DOTALL)
    source_count = 0
    if sources_match:
        sources_block = sources_match.group(1)
        source_count = len(re.findall(r'- "\[\[', sources_block))
    
    # Add source_count, status, created, aliases before updated:
    additions = f"status: seed\ncreated: 2026-07-15\nsource_count: {source_count}\naliases: []\n"
    content = content.replace("updated:", additions + "updated:")
    
    # Remove title: "..."
    content = re.sub(r'title: ".*?"\n', '', content)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {file}")
