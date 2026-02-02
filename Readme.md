# Personal AI Operating System

It's a fun learning project to learn about LangChain, LangGraph and MCP Servers. And Enhance my skill/proficiency in python.

## Technologies used:

1. **MCP Server:** it create a standard way for the models to interact with servers that hold real-world data or perform useful tasks.
2. **Playwright:** Browser automation engine( it's used as an MCP tool).
3. **LangChain:** it's used for giving access tools to ai agents. basically, it answers: "How do I let an LLM call tools?”
4. **LangGraph:** it let u decide node and edges like a flowchart, Each node can represent a task, an action or a model call. This structure allows loops, branching, and parallel paths. It’s perfect for building agent-like systems where the model reasons, decides, and acts.
5. **Ollama:**
6. **RAG (Retrival Augmented Learning):** Model memory for calling MCP Server correctly, or to decide which tool to call at inference time.

7. **Python:**

### LangChain Tools

- MCP SERVER (FASTMCP): Create an interface for the ai brain, like call function or something
- Playwright:
- OS
- APIs

### Here's how RAG with MCP Server is going to work:

First, The JSON that MCP Server send is split into small chunks. Each chunk is converted into a vector embedding. These embeddings are stored in a vector database.

Second, when a user asks a question, that question is also converted into an embedding. The system searches the vector database to find the most similar chunks.

Third, those chunks are sent to the language model along with the question. The model uses only that context to generate an answer.

with this, qwen2.5:4b-instruct model can control hundered of tools, while, only having a contex window of 4096 tokens.

### Who Can Contribute:

**Required Knowledge**

- Basic to intermediate Python

- Understanding of Object-Oriented Programming (OOP)

- Familiarity with Git & GitHub (clone, branch, commit, pull requests)

- Know how to read Documentation

**Recommended Before Contributing**

- Read the reference articles listed below

**Basic understanding of:**

- LangChain tool-calling concepts

- LangGraph workflow graphs

- MCP (Model Context Protocol) idea

**Good to Have**

- Experience with browser automation (Playwright or Selenium)
- Familiarity with APIs and async programming
- Interest in AI agent systems

**Contribution Expectations**

- Write clean, readable code
- Add brief comments where logic is non-obvious
- Test changes before submitting a PR
- Keep commits descriptive

**Models**
When run locally on intel i5 13th gen, with 6 cores

- deepseek-coder:6.7b: memory usage: 13GB SSD(Swaparea used as RAM) + 7.5GB RAM = 20.5GB, token per second on WSL: 10 token/s, token per seconds on Windows: 7-8 token/s
- phi3:mini: memory usage: 7.5 GB RAM + 6.3GB SSD(Swaparea used as RAM) = 13.8 GB, token per seconds on WSL: 110 token/s, token per seconds on Windows: 45 token/s

### References(articles):

1.  > How to Use LangChain and LangGraph: A Beginner’s Guide to AI Workflows: https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/
2.  > Langchain & LangGraph Documentation: https://docs.langchain.com/oss/python/langchain/agents
3.  > Check Out How to Build and Deploy an AI Agent with LangChain, FastAPI, and Sevalla: https://www.freecodecamp.org/news/build-ai-agent-with-langchain-fastapi-and-sevalla/
4.  > Checkout how to use mcp server: https://www.freecodecamp.org/news/how-to-build-your-first-mcp-server-using-fastmcp/#heading-using-the-mcp-server-with-an-llm-application
5.  > Understanding MCP and its working: https://medium.com/@SrGrace_/understanding-model-context-protocol-mcp-a-laymans-guide-4737aab5fc6b
6.  > Understand how to setup model locally using ollama: https://medium.com/%40bluudit/deploy-llms-locally-with-ollama-your-complete-guide-to-local-ai-development-ba60d61b6cea
7.  > Different ways to run model locally and requirements: https://skywork.ai/blog/llm/ollama-windows-guide-install-run-local-ai-on-pc/?utm_source=chatgpt.com#method-2-wsl2-advanced
8.  > Ollama Docs: https://docs.ollama.com/faq#how-can-i-view-the-logs
9.  > Role of vector store in memory: https://www.freecodecamp.org/news/how-ai-agents-remember-things-vector-stores-in-llm-memory/
10. > Sentence_transformers quickstart guide: https://www.sbert.net/docs/quickstart.html
11. > Faiss vector databases: https://www.geeksforgeeks.org/data-science/what-is-faiss/
