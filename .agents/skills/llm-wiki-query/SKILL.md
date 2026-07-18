---
name: llm-wiki-query
description: Queries the LLM-Wiki for information, relying strictly on the catalog and wiki notes.
---

# LLM-Wiki Query Skill

**Role**: You are responsible for retrieving knowledge from the wiki.

**Instructions**:
1. Always search `Wiki/catalog.jsonl` first.
2. Follow links to `Wiki/` notes to gather context.
3. Do not invent citations or claims. Base your answers strictly on the wiki content.
