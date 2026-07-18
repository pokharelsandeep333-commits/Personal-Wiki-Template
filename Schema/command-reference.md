# Command Reference

## `scripts/wiki_tool.py` Commands

- `doctor`: Runs a non-mutating health check for folders, Python version, catalog existence, source manifest, and basic note counts.
- `build`: Generates `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder index files.
- `lint`: Validates compiled Wiki note frontmatter, ensures tags are allowed, source links resolve correctly, and `source_count` matches.
- `source-scan`: Lists Raw sources in the vault.
- `source-scan --update --accept-covered`: Updates the source manifest after Wiki notes cover Raw sources.
- `source-lint`: Validates source frontmatter rules and source coverage state.
- `source-delta`: Shows Raw sources not represented in the manifest.
- `source-coverage`: Shows which Raw sources are covered by compiled Wiki notes.
- `search-catalog --query "text"`: Searches compiled Wiki notes through the catalog.
- `log --title "title" --details "details"`: Appends a short entry to `Wiki/log.md`.

## `scripts/audit_public.py`
Scans the repository during pre-commit to fail on obvious secrets, machine-local paths, private keys, and plugin/cache state tracking.
