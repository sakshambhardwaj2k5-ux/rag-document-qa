# RAG-Based PDF Question Answering System

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to ask questions about PDF documents and receive answers grounded in the retrieved document context.

## Overview

This project implements a basic RAG pipeline using Python, LangChain, ChromaDB, HuggingFace embeddings, and Google's Gemini LLM.

Instead of relying entirely on an LLM's pretrained knowledge, the application retrieves relevant information from PDF documents and uses that information to generate context-aware answers.

## Architecture

```text
PDF Documents
     |
     v
Document Loading
     |
     v
Text Chunking
     |
     v
HuggingFace Embeddings
     |
     v
ChromaDB Vector Store
     |
     v
Similarity Retrieval
     |
     v
Retrieved Context + User Query
     |
     v
Gemini LLM
     |
     v
Generated Answer
```

## Tech Stack

- **Language:** Python
- **LLM:** Google Gemini
- **Framework:** LangChain
- **Embeddings:** HuggingFace (`sentence-transformers/all-mpnet-base-v2`)
- **Vector Database:** ChromaDB
- **Package Management:** uv

## Project Structure

```text
rag-document-qa/
│
├── data/
│   └── pdfs/
│
├── src/
│   └── rag_tut/
│       ├── __init__.py
│       ├── document_processor.py
│       ├── vector_store_manager.py
│       ├── query_retrieval.py
│       ├── llm_service.py
│       └── rag_pipeline.py
│
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

## Core Components

| Component | Responsibility |
|---|---|
| DocumentProcessor | Loads and processes PDF documents |
| VectorStoreManager | Manages embeddings and ChromaDB |
| QueryAndRetrieval | Retrieves relevant document chunks |
| LLMService | Initializes and interacts with Gemini |
| RAGPipeline | Orchestrates the RAG workflow |

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sakshambhardwaj2k5-ux/rag-document-qa.git
cd rag-document-qa
```

### 2. Install dependencies

Using uv:

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

### 4. Add PDF documents

Place your PDF documents inside:

```text
data/pdfs/
```

### 5. Run the application

```bash
uv run python main.py
```

## Current Capabilities

- PDF document ingestion
- Text splitting into manageable chunks
- Semantic embeddings using HuggingFace
- Vector storage using ChromaDB
- Similarity-based document retrieval
- Context-grounded answer generation using Gemini

## Future Improvements

- Source citations and page-level references
- Web-based user interface
- Support for additional document formats
- Improved retrieval and reranking
- Conversation history and multi-turn question answering

## Author

**Saksham Bhardwaj**

[GitHub](https://github.com/sakshambhardwaj2k5-ux)
