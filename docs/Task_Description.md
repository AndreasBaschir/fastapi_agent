# LLM Developer Task: Summarization API with LLM Tool Integration

Dear candidate,

thank you very much for the pleasant interview. We would like you to take the next step in our recruiting process and to demonstrate your practical skills for this position on the example of a (small) AI-based service / agent tool.

## Objective

Build a **FastAPI-based summarization microservice** in Python that:

- Uses a **real LLM API** (e.g., OpenAI or Gemini) to generate the summaries
- Supports different **lengths**, **styles**, and **focus topics**
- Is callable as a **tool by LangChain or LlamaIndex agents**
- _The creation of the agent itsself or a demo how to use it in tool calling is optional_

---

## Implementation Requirements

### 1. FastAPI Service

Build a FastAPI application with one POST endpoint:

```
POST /summarize
```

#### Request Schema:

```json
{
  "text": "...",
  "length": "short|medium|long",
  "style": "bullet|paragraph|numbered",
  "focus": "optional topic to emphasize"
}
```

#### Example Response Schema:

```json
{
  "summary": "...",
  "meta": {
    "tokens": 260,
    "length": "...",
    "style": "...",
    "focus": "..."
  }
}
```

**The Python version, fastAPI and pydantic versions you use don't matter. However, use versions that are compatible to each other.**

### 2. Summarization Logic

- You must use a **real LLM** (like OpenAI's GPT or Gemini via Vertex AI) or a local version (e.g. downloadable from HuggingFace)
- The prompt must reflect the given input parameters

**Prompt engineering is part of the task.**

### 3. Tool Calling Compatibility (for LangChain or LlamaIndex)

Describe how you would make your API callable via either:

- **LangChain `RequestsPostTool`** or
- **LlamaIndex `FunctionTool`**
- Optional (Bonus): Wrap your API into an own LangChain or LlamaIndex agent and demonstrate the usage
  on the following user input and one of the example texts.

```
Please summarize the following text in a short manner (less than 200 words) in bullet points, specifically focusing
on the costs for using LLMs.
```

---

## Test data

Use one of the three provided example articles in folder _examples_ to test your prompt & the web service.

---

## Documentation

Include a `README.md` with:

- Setup instructions
- API endpoint description and examples
- Explanation of how it integrates as a tool with LangChain or LlamaIndex
- Optional: brief reasoning on your prompt design and how to adapt the prompt

---

## Bonus Points

All following tasks are **optional**.
You will earn extra credit for:

- Containerized deployment in a docker container (`Dockerfile`)
- Unit tests for the FastAPI route and summarization logic
- Jupyter notebook showcasing API usage
- Basic LangChain or LlamaIndex agent calling your service
- Logging, retries, or rate limit handling for LLM API

---

## Submission

Submit via GitHub in a private repository or via exported zip of the repo:

- Source code
- README.md
- Optional: notebook, tests, Dockerfile

**IMPORTANT**: **DO NOT SEND US YOUR OPENAI OR SIMILAR CLOUD SECRETS**.
You can use ENV variables and we can use our own keys for this.

---

## Evaluation Criteria

We will evaluate your solution with a focus on:

- Clean, easy to read Python code
- Documentation of your work approach and the code
- Correct use of Fast API and schema handling
- Prompt template and its quality
- Bonus: dockerization, tests, agent demo

---
