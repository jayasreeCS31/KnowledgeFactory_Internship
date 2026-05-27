# Day 3 – RAG Pipeline using ChromaDB

## Overview

This project demonstrates a basic Retrieval-Augmented Generation (RAG) workflow using PDF documents and semantic search.

The system:

- Reads PDF documents
- Extracts text
- Splits text into chunks
- Converts chunks into embeddings
- Stores embeddings in ChromaDB
- Retrieves semantically relevant content

---

## Project Structure

day3_rag/

├── sample.pdf

├── pdf_reader.py

├── chunking.py

├── embeddings.py

├── semantic_search.py

├── rag_pipeline.py

├── requirements.txt

├── .gitignore

└── README.md

---

## Technologies Used

- Python
- PyPDF
- Sentence Transformers
- ChromaDB
- NumPy

---

## Workflow

PDF

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

ChromaDB Storage

↓

Semantic Search

↓

Retrieved Answer

---

## Learning Outcome

Implemented a mini enterprise RAG pipeline and understood document ingestion, embeddings, vector databases, and semantic retrieval.