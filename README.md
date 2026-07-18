# 🧠 Agentic LLM-Wiki Template

[![Obsidian](https://img.shields.io/badge/Obsidian-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white)](https://obsidian.md/)
[![AI Powered](https://img.shields.io/badge/AI_Powered-000000?style=for-the-badge&logo=openai&logoColor=white)](#)

A fully structured, intelligent Obsidian Vault template designed for AI Agentic workflows. This repository serves as a powerful knowledge base that your LLM assistants can ingest, maintain, and query autonomously.

## ✨ Features
* **Structured Knowledge Base:** Strict separation of `Raw/` sources from compiled `Wiki/` knowledge.
* **Agent Skills Included:** Comes pre-configured with a `.agents/` folder containing specialized skills (`llm-wiki-ingest`, `llm-wiki-lint`, `llm-wiki-query`).
* **Schema Enforcement:** Defined frontmatter schemas and linting checklists to keep your knowledge base perfectly organized.
* **Automated Python Utilities:** Built-in scripts for managing large files, fixing schemas, and auditing the vault.

---

## 🚀 Getting Started

### 1. Clone the Repository
Download this repository to your local machine:
```bash
git clone https://github.com/your-username/llm-wiki-template.git
```

### 2. Open in Obsidian
1. Download and install [Obsidian](https://obsidian.md/).
2. Open Obsidian and select **"Open folder as vault"**.
3. Select the folder you just cloned.

### 3. Smart Plugins & AI Capabilities
This template is configured to work with advanced AI community plugins (such as **Smart Connections**, **Smart Context**, and **Smart ChatGPT**). 

To enable the full semantic search and AI connection features:
1. Open Obsidian **Settings** > **Community Plugins**.
2. Turn off "Safe Mode" if prompted, and enable the Smart plugins that are pre-installed in this vault.
3. Once enabled, the Smart plugin will automatically generate a `.smart-env` folder in your vault. This folder will securely store your local vector embeddings and AI configuration data.

*(Note: Do not commit the generated `.smart-env` folder to a public repository if it contains your personal embeddings! The provided `.gitignore` handles this automatically by only allowing the folder but you should still be careful).*

---

## 📂 Architecture & Workflow

This Wiki uses a strict **Raw → Wiki** pipeline to maintain high-quality knowledge.

* `Raw/`: Your dumping ground. Put raw PDFs, articles, web clippings, and rough thoughts here.
* `Wiki/`: The compiled, polished truth. AI agents read your `Raw` files and extract entities, concepts, and topics into the `Wiki`.
* `Schema/`: The rulebook for how notes should be formatted. Agents read this before making changes.

### Example Workflow
1. **Save a source:** Save an article to `Raw/Sources/My Article.md`.
2. **Command your Agent:** Ask your AI assistant to "Ingest 'My Article.md'".
3. **Review:** The agent will process the source, extract the core ideas, and generate perfectly formatted files in `Wiki/Concepts/` and `Wiki/Entities/`.
4. **Explore:** Everything is interlinked automatically using Obsidian's `[[wikilinks]]`.

We've included an `Agentic Workflows` concept and an `Example Source` in the vault so you can see how they are structured!

---

## 🤖 Using the Agent Skills
If you use AI IDEs or CLI agents that support the standard `.agents` specification, this repository is ready out of the box. 

When your agent opens this directory, it will automatically load the skills in the `.agents/` folder, teaching it exactly how to ingest, lint, and query this specific Wiki structure without you needing to explain it!
