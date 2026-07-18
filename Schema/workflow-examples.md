# Workflow Examples

### Ingestion Workflow
1. Place raw text or files into `Raw/Sources/`.
2. Extract key entities and concepts.
3. Create atomic notes in `Wiki/Concepts/` and `Wiki/Entities/`.
4. Link back to the original source in `Raw/Sources/`.

### Maintenance Workflow
1. Periodically run the lint checklist.
2. Update `Wiki/catalog.jsonl` with new entries.
