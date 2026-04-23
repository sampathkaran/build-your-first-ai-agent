# 🚀 Project Setup & Usage Guide

This repository contains a pipeline for ingestion, embedding storage, and a UI interface for querying results.

---

# 📦 1. Prerequisites

Make sure you have:

- Python 3.10+

---

# ⚡ 2. Install UV (Fast Python Package Manager)

We use **uv** to manage dependencies and environments.

## 🍎 macOS Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 🐧 Linux Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

# 📥 3. Install Dependencies
Clone the repository:

```bash
git clone https://github.com/sampathkaran/build-your-first-ai-agent.git
cd build-your-first-ai-agent
```

Now install dependencies:

```bash
uv sync
``` 

What this does:
- Creates a virtual environment automatically
- Installs all dependencies from pyproject.toml
- Locks exact versions using uv.lock

# 4. UV Project Files Explained
🧾 pyproject.toml

This file contains:

- Project metadata
- Dependency list
- Python version requirements

👉 This is the source of truth for dependencies.

🔒 uv.lock

This file contains:

- Exact resolved dependency versions
- Ensures reproducible environments

👉 Think of it as a frozen snapshot of your environment.

# 5. 🔐 Environment Variables Setup
You will find a file:

```bash
.env-example
```
Rename it to:

```bash
.env
```
Then update it with your API keys:
```bash
OPENAI_API_KEY="PASTE YOUR OPENAI API KEY HERE"
TAVILY_API_KEY="PASTE YOUR TAVILY API KEY HERE"
personal_access_token="PASTE YOUR GITHUB PAT TOKEN"
```
# 6. 🧠 Run the python file to demo the basic llm call

```bash
uv run python 1_basic_llm_call.py
```

# 7. 🧠 Run the python file to demo the basic llm chatbot

```bash
uv run python 2_basic_llm_chatbot.py
```

# 8. 🧠 Run the python file to demo the agent
```bash
uv run python 3_create_agent.py
```
# 8. 🧠 Run the python file to demo the agent using google model - use this incase you wish to no pay for openai models
```bash
uv run python 4_create_agent_google.py
```
