import os, sys, json, re, argparse, datetime

ALLOWED_TAGS = {"topic", "concept", "entity", "project", "log"}

def parse_frontmatter(content):
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match: return None
    fm_text = match.group(1)
    data = {}
    current_key = None
    for line in fm_text.splitlines():
        if not line.strip(): continue
        if line.startswith('  -'):
            if current_key and isinstance(data.get(current_key), list):
                val = line.strip()[1:].strip().strip('"').strip("'")
                data[current_key].append(val)
        elif ':' in line:
            k, v = line.split(':', 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if not v:
                data[k] = []
                current_key = k
            elif v.startswith('[') and v.endswith(']'):
                items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(',') if x.strip()]
                data[k] = items
            else:
                data[k] = v
                current_key = k
    return data

def get_wiki_notes():
    notes = []
    if not os.path.exists('Wiki'): return notes
    for root, _, files in os.walk('Wiki'):
        for f in files:
            if f.endswith('.md') and f not in ('index.md', 'log.md'):
                notes.append(os.path.join(root, f).replace('\\', '/'))
    return notes

def get_raw_sources():
    sources = []
    if not os.path.exists('Raw/Sources'): return sources
    for root, _, files in os.walk('Raw/Sources'):
        for f in files:
            if f.endswith('.md'):
                sources.append(os.path.join(root, f).replace('\\', '/'))
    return sources

def build():
    notes = get_wiki_notes()
    catalog = []
    folders = set()
    os.makedirs('Wiki', exist_ok=True)
    for path in notes:
        with open(path, 'r', encoding='utf-8') as f:
            fm = parse_frontmatter(f.read()) or {}
        tags = fm.get('tags', [])
        tag = tags[0] if tags else ""
        catalog.append({
            "path": path,
            "title": fm.get('title', os.path.basename(path).replace('.md', '')),
            "tag": tag,
            "topics": fm.get('topics', []),
            "sources": fm.get('sources', []),
            "updated": fm.get('updated', datetime.date.today().isoformat())
        })
        folders.add(os.path.dirname(path))
    
    with open('Wiki/catalog.jsonl', 'w', encoding='utf-8') as f:
        for c in catalog: f.write(json.dumps(c) + '\n')
            
    with open('Wiki/index.md', 'w', encoding='utf-8') as f:
        f.write("# Wiki Index\n\n")
        for c in catalog: f.write(f"- [{c['title']}](../{c['path']})\n")
            
    for folder in folders:
        with open(f'{folder}/index.md', 'w', encoding='utf-8') as f:
            f.write(f"# Index for {folder}\n\n")
            for c in catalog:
                if c['path'].startswith(folder):
                    f.write(f"- [{c['title']}](./{os.path.basename(c['path'])})\n")
    print("Build complete.")

def lint():
    notes = get_wiki_notes()
    raw_sources = get_raw_sources()
    errors = 0
    for path in notes:
        with open(path, 'r', encoding='utf-8') as f:
            fm = parse_frontmatter(f.read())
        if not fm:
            print(f"LINT FAIL: {path} has no valid frontmatter.")
            errors += 1
            continue
        
        tags = fm.get('tags', [])
        if not tags or not set(tags).intersection(ALLOWED_TAGS):
            print(f"LINT FAIL: {path} must have one of allowed tags: {ALLOWED_TAGS}")
            errors += 1
            
        sources = fm.get('sources', [])
        scount = int(fm.get('source_count', 0))
        if len(sources) != scount:
            print(f"LINT FAIL: {path} source_count ({scount}) != length of sources ({len(sources)})")
            errors += 1
            
        for s in sources:
            s_name = s.replace('[[', '').replace(']]', '').replace('.md', '')
            found = any(s_name in rs for rs in raw_sources)
            if not found:
                print(f"LINT FAIL: {path} source link {s} does not resolve in Raw/Sources/")
                errors += 1
                
    if errors > 0: sys.exit(1)
    print("Lint passed.")

def doctor():
    print(f"Python Version: {sys.version}")
    print(f"Wiki notes count: {len(get_wiki_notes())}")
    print(f"Raw sources count: {len(get_raw_sources())}")
    print(f"Catalog exists: {os.path.exists('Wiki/catalog.jsonl')}")
    print(f"Source manifest exists: {os.path.exists('Schema/source-manifest.jsonl')}")

def source_scan(update=False, accept_covered=False):
    sources = get_raw_sources()
    catalog = []
    if os.path.exists('Wiki/catalog.jsonl'):
        with open('Wiki/catalog.jsonl', 'r', encoding='utf-8') as f:
            catalog = [json.loads(line) for line in f if line.strip()]
            
    manifest_dict = {}
    if os.path.exists('Schema/source-manifest.jsonl'):
        with open('Schema/source-manifest.jsonl', 'r', encoding='utf-8') as f:
            manifest = [json.loads(line) for line in f if line.strip()]
            manifest_dict = {m['path']: m for m in manifest}
            
    for path in sources:
        with open(path, 'r', encoding='utf-8') as f:
            fm = parse_frontmatter(f.read()) or {}
        title = fm.get('Title', os.path.basename(path).replace('.md', ''))
        path_base = os.path.basename(path).replace('.md', '')
        
        covered_by = []
        for c in catalog:
            for s in c.get('sources', []):
                if path_base in s: covered_by.append(c['path'])
                    
        processed = str(fm.get('Processed', 'false')).lower() == 'true'
        if update:
            manifest_dict[path] = {
                "path": path, "title": title, "processed": processed,
                "covered_by": covered_by, "updated": datetime.date.today().isoformat()
            }
            
    if update:
        os.makedirs('Schema', exist_ok=True)
        with open('Schema/source-manifest.jsonl', 'w', encoding='utf-8') as f:
            for path in sorted(manifest_dict.keys()):
                f.write(json.dumps(manifest_dict[path]) + '\n')
        print("Manifest updated.")
    else:
        for path in sources: print(f"Scanned {path}")

def source_lint():
    sources = get_raw_sources()
    errors = 0
    catalog = []
    if os.path.exists('Wiki/catalog.jsonl'):
        with open('Wiki/catalog.jsonl', 'r', encoding='utf-8') as f:
            catalog = [json.loads(line) for line in f if line.strip()]
            
    for path in sources:
        with open(path, 'r', encoding='utf-8') as f:
            fm = parse_frontmatter(f.read())
        if not fm:
            print(f"SOURCE-LINT FAIL: {path} lacks valid frontmatter")
            errors += 1
            continue
            
        for req in ['Title', 'Reference', 'Created', 'Processed', 'tags']:
            if req not in fm:
                print(f"SOURCE-LINT FAIL: {path} missing {req}")
                errors += 1
                
        processed = str(fm.get('Processed', 'false')).lower() == 'true'
        if processed:
            path_base = os.path.basename(path).replace('.md', '')
            covered = any(path_base in s for c in catalog for s in c.get('sources', []))
            if not covered:
                print(f"SOURCE-LINT FAIL: {path} marked processed but has no Wiki coverage")
                errors += 1
                
    if errors > 0: sys.exit(1)
    print("Source lint passed.")

def source_delta():
    sources = set(get_raw_sources())
    manifest_sources = set()
    if os.path.exists('Schema/source-manifest.jsonl'):
        with open('Schema/source-manifest.jsonl', 'r', encoding='utf-8') as f:
            manifest = [json.loads(line) for line in f if line.strip()]
            manifest_sources = {m['path'] for m in manifest}
    delta = sources - manifest_sources
    if delta:
        print("Sources not in manifest:"); [print(d) for d in delta]
    else:
        print("No delta.")

def source_coverage():
    sources = get_raw_sources()
    catalog = []
    if os.path.exists('Wiki/catalog.jsonl'):
        with open('Wiki/catalog.jsonl', 'r', encoding='utf-8') as f:
            catalog = [json.loads(line) for line in f if line.strip()]
    for path in sources:
        path_base = os.path.basename(path).replace('.md', '')
        covered_by = [c['path'] for c in catalog if any(path_base in s for s in c.get('sources', []))]
        print(f"{path}: Covered by {len(covered_by)} notes.")

def search_catalog(query):
    if not os.path.exists('Wiki/catalog.jsonl'): return
    with open('Wiki/catalog.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            if query.lower() in line.lower(): print(json.loads(line)['path'])

def log_entry(title, details):
    os.makedirs('Wiki', exist_ok=True)
    with open('Wiki/log.md', 'a', encoding='utf-8') as f:
        f.write(f"\n## {datetime.datetime.now().isoformat()} - {title}\n{details}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('doctor')
    subparsers.add_parser('build')
    subparsers.add_parser('lint')
    scan_p = subparsers.add_parser('source-scan')
    scan_p.add_argument('--update', action='store_true')
    scan_p.add_argument('--accept-covered', action='store_true')
    subparsers.add_parser('source-lint')
    subparsers.add_parser('source-delta')
    subparsers.add_parser('source-coverage')
    search_p = subparsers.add_parser('search-catalog')
    search_p.add_argument('--query', required=True)
    log_p = subparsers.add_parser('log')
    log_p.add_argument('--title', required=True)
    log_p.add_argument('--details', required=True)
    
    args = parser.parse_args()
    if args.command == 'doctor': doctor()
    elif args.command == 'build': build()
    elif args.command == 'lint': lint()
    elif args.command == 'source-scan': source_scan(args.update, args.accept_covered)
    elif args.command == 'source-lint': source_lint()
    elif args.command == 'source-delta': source_delta()
    elif args.command == 'source-coverage': source_coverage()
    elif args.command == 'search-catalog': search_catalog(args.query)
    elif args.command == 'log': log_entry(args.title, args.details)
