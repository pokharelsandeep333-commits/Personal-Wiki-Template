# Agent Rules and Guidelines

When working in this LLM-Wiki, agents MUST adhere to the following rules:

1. Treat `Raw/Sources/` as source material, not as compiled notes.
2. Write reusable knowledge only under `Wiki/`.
3. Keep every compiled note linked to one or more Raw sources.
4. Search `Wiki/catalog.jsonl` before opening broad Raw context.
5. Run build, lint, and source checks before commits.
6. Do not invent citations or create unsupported claims.
7. Truncation Safety: When using the view_file tool, if the output indicates the content was truncated at 46080 bytes, you MUST automatically call the tool again using the ContentOffset parameter to read the next chunk. You must loop this process until you have read the entire file before you attempt to summarize it, extract concepts from it, or take any final actions.
