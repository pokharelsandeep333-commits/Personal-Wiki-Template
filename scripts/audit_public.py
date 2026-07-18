import os, sys, re

def audit():
    patterns = {
        'API Key or Secret': r'(?i)(api_key|secret|password|token)\s*[:=]\s*["\'][a-zA-Z0-9_\-]{16,}["\']',
        'Private Key': r'-----BEGIN (RSA|OPENSSH|DSA|EC|PGP) PRIVATE KEY-----',
        'Machine-Local Path': r'(?i)(C:\\Users\\[^\\]+|/Users/[^/]+|/home/[^/]+)',
        'Plugin/Cache State': r'\.obsidian/(workspace\.json|workspace-mobile\.json)'
    }
    
    errors = 0
    for root, dirs, files in os.walk('.'):
        if '.git' in root or '.obsidian' in root: continue
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    for name, regex in patterns.items():
                        if re.search(regex, content):
                            if name == 'Plugin/Cache State' and f == '.gitignore': continue
                            if name == 'Machine-Local Path' and ('audit_public.py' in f or 'recover.js' in f): continue
                            print(f"AUDIT FAIL: {path} contains {name}")
                            errors += 1
            except UnicodeDecodeError:
                pass
    if errors > 0: sys.exit(1)
    print("Audit passed.")

if __name__ == '__main__':
    audit()
