# RAG-Powered Complaint Chatbot

## Project Overview
This project builds a Retrieval-Augmented Generation (RAG) chatbot for CrediTrust Financial to transform customer complaints into actionable insights.

## Business Problem
CrediTrust receives thousands of customer complaints monthly but lacks an efficient way to analyze them. Product managers spend hours manually reading complaints to identify trends.

## Solution
A RAG-powered chatbot that:
1. Retrieves relevant complaint narratives using semantic search
2. Generates concise, evidence-backed answers using LLMs
3. Provides a user-friendly interface for non-technical teams

## Project Structure
rag-complaint-chatbot/
├── data/ # Data storage
│ ├── raw/ # Original CFPB dataset
│ └── processed/ # Cleaned and processed data
├── vector_store/ # FAISS/ChromaDB indices
├── notebooks/ # Jupyter notebooks for tasks
├── src/ # Source code modules
├── tests/ # Unit tests
├── app.py # Gradio/Streamlit interface
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## Tasks Completed

### Task 1: Exploratory Data Analysis and Preprocessing
- Loaded and analyzed CFPB complaint dataset
- Filtered for target products (Credit Cards, Personal Loans, Savings Accounts, Money Transfers)
- Cleaned text narratives (lowercasing, removing boilerplate, special characters)
- Saved cleaned data to `data/processed/filtered_complaints.csv`

### Task 2: Text Chunking, Embedding, and Vector Store
- Created stratified sample of 12,000 complaints
- Implemented text chunking with optimal parameters (chunk_size=500, overlap=50)
- Generated embeddings using all-MiniLM-L6-v2 model
- Built both FAISS and ChromaDB vector stores with metadata

## How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

   Run Task 1 notebook:

bash
jupyter notebook notebooks/task1_eda_preprocessing.ipynb
Run Task 2 notebook:

bash
jupyter notebook notebooks/task2_chunking_embedding.ipynb
Key Findings
From Task 1 EDA:
Dataset contains complaints across multiple financial products

Most narratives are 50-200 words long

Some narratives contain boilerplate text requiring cleaning

Filtered dataset focuses on CrediTrust's core products

From Task 2:
Optimal chunking: 500 characters with 50-character overlap

all-MiniLM-L6-v2 provides efficient embeddings (384 dimensions)

Both FAISS and ChromaDB successfully index and retrieve relevant chunks

Metadata is preserved for traceability