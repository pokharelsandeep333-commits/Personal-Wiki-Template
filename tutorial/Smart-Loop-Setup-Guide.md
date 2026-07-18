# The Smart Loop Setup Guide

This guide breaks down exactly how to install and use the 3-step "Smart Loop" workflow in your Obsidian vault, as detailed in the video.

## Step 1: Install the Core Foundation
The entire workflow relies on the **Smart Environment**, a shared local vector database. You must install the primary plugin first.

1. Open Obsidian **Settings** > **Community plugins**.
2. Click **Browse** and search for **Smart Connections**.
3. Install and Enable it. 
4. *Important:* Let it run in the background. It needs a few minutes to read your vault and convert all your notes into mathematical embeddings.
5. In the bottom right corner of Obsidian, you will now see a **Smart Environment** button. Click it and select **Show Stats** to verify it is working.

---

## Step 2: Install Context & Chat
Once the core is installed, you need to enable the two sister plugins (Context and Chat).

1. Click the **Smart Environment** button in the bottom right corner.
2. Scroll down to **Browse Smart Plugins**.
3. Find **Context Core** and click **Install**.
4. Find **Chat Core** (formerly Smart ChatGPT) and click **Install**.
5. Reload Obsidian (you can use `Ctrl/Cmd + P` and type "Reload app without saving").

---

## Step 3: The "Smart Project Template"
To make the loop effortless, the video recommends creating a template that automatically inserts the UI blocks for these plugins into your notes.

> [!TIP]
> **I have already done this step for you!** I created a new file in your vault at `_templates/Smart Project Template.md`. 
>
> You can now apply this template to any new project note to instantly inject the Smart Loop interface.

---

## How to Actually Use the Workflow (The Loop)

When you start a new project, apply the **Smart Project Template**. Here is how you use the three blocks that appear:

### Phase 1: Discover
Start typing your ideas or research into the top of the note. As you type, the ```` ```smart-connections ``` ```` block will magically update in real-time. It will show you a list of the most semantically related notes from across your entire vault.

### Phase 2: Bundle
Once the Smart Connections block finds highly relevant notes, you want to save them.
1. Click the button inside the connections block that says **Send Results to Smart Context**.
2. This creates a "Named Context" bundle in the ```` ```smart-context ``` ```` block.
3. You can click into this bundle and **prune** it (remove notes that aren't quite right). You now have a concentrated, reusable bundle of context.

### Phase 3: AI Chat
Now you want to ask AI to help you, without it hallucinating.
1. Go down to the ```` ```smart-chat ``` ```` block.
2. Inside the chat window, click the **Build Context** button. This instantly pastes your entire curated Context Bundle into the chat.
3. Ask your question (e.g., *"Based on this context, what should my priorities be?"*).
4. **The Magic:** The chat thread is now permanently hard-linked to this specific project note. You will never lose the conversation history.

### Completing the Loop
When the AI gives you a great answer, copy the best insights out of the chat and paste them into the top of your project note. Because you added new text, the **Smart Connections** block will immediately re-read your note, update the embeddings, and start finding *even more* related notes for you to explore!
