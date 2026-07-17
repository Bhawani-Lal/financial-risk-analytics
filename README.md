# 🧠 AI Document Intelligence Tool

> **RAG-powered document Q&A system** — upload business documents, ask questions in plain English, get answers cited to the source.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Claude API](https://img.shields.io/badge/Claude_API-Anthropic-D97706?style=flat)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat&logo=react&logoColor=black)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 🔍 What It Does

Most AI chatbots answer from general training data — confident, unverifiable, and often wrong about *your* documents.

This tool is different. It reads **only your documents**, retrieves the most relevant passages, and generates answers **cited to the exact source chunk**. Every answer is checkable. Every claim is traceable.

**Target use-case:** Business analysts, consultants, and knowledge workers who need to interrogate large document sets — reports, PDFs, policy documents, research — without reading every page.

> Inspired by the document intelligence workflows used by McKinsey Digital and similar firms in AI-driven knowledge management.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    React Frontend                    │
│         Upload · Query · Structured Results          │
└───────────────────┬─────────────────────────────────┘
                    │ HTTP
┌───────────────────▼─────────────────────────────────┐
│                  FastAPI Backend                     │
│                                                      │
│  ┌─────────────┐    ┌──────────────┐                │
│  │  Ingestion  │    │  Query Layer │                │
│  │  Pipeline   │    │              │                │
│  │             │    │  Semantic    │                │
│  │ PDF → Chunk │    │  Retrieval   │                │
│  │ → Embed →   │    │  → Claude    │                │
│  │ Vector Store│    │  API → Answer│                │
│  └─────────────┘    └──────────────┘                │
└─────────────────────────────────────────────────────┘
```

**Pipeline steps:**
1. **Ingest** — Upload PDF/text documents via the React frontend
2. **Chunk** — Semantic chunking splits documents intelligently at paragraph/section boundaries
3. **Embed** — Chunks are embedded and stored in a local vector store
4. **Retrieve** — On query, top-k most relevant chunks are retrieved by cosine similarity
5. **Generate** — Claude API synthesises a grounded answer from retrieved context only
6. **Cite** — Every answer references the source chunk and page number

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 Multi-document upload | Ingest multiple PDFs or text files in one session |
| 🔍 Semantic search | Vector similarity retrieval — finds meaning, not just keywords |
| 🤖 Claude-powered answers | Anthropic's Claude generates fluent, grounded responses |
| 📌 Source citations | Every answer cites the retrieved chunk and document |
| ❌ Hallucination guardrails | Model is instructed to say "not found" rather than invent |
| 🖥️ Clean React UI | Document upload, query box, and structured insight extraction |
| ⚡ FastAPI backend | Async REST API — fast, lightweight, production-ready structure |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React 18, Tailwind CSS |
| **Backend** | Python, FastAPI |
| **RAG Pipeline** | LangChain |
| **LLM** | Claude API (Anthropic) — `claude-sonnet-4-6` |
| **Embeddings** | sentence-transformers / OpenAI embeddings |
| **Vector Store** | FAISS (local) |
| **Document Parsing** | PyMuPDF / pdfplumber |
| **Deployment** | Railway / Render |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- Anthropic API key ([get one here](https://console.anthropic.com))

### 1. Clone the repo
```bash
git clone https://github.com/Bhawani-Lal/ai-document-intelligence.git
cd ai-document-intelligence
```

### 2. Set up the backend
```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file:
```env
ANTHROPIC_API_KEY=your_api_key_here
```

Run the FastAPI server:
```bash
uvicorn main:app --reload
```

### 3. Set up the frontend
```bash
cd frontend
npm install
npm run dev
```

### 4. Open the app
Navigate to `http://localhost:5173` — upload a document and start querying.

---

## 📁 Project Structure

```
ai-document-intelligence/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── ingestion.py         # Document parsing & chunking pipeline
│   ├── embeddings.py        # Vector embedding & FAISS store
│   ├── retrieval.py         # Semantic search & top-k retrieval
│   ├── generation.py        # Claude API integration & prompt logic
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── DocumentUpload.jsx
│   │   │   ├── QueryBox.jsx
│   │   │   └── AnswerPanel.jsx
│   └── package.json
├── docs/
│   └── architecture.png
└── README.md
```

---

## 💡 Example Usage

**Upload:** Annual report PDF (150 pages)

**Query:**
> "What were the key risk factors identified in Q3 and how did management respond?"

**Response:**
> Three primary risk factors were identified in Q3: supply chain disruption, rising interest rates, and regulatory changes in the EU market. Management responded by... **[Source: Page 47, Section 3.2 — Risk Management]**

---

## 🎯 Use Cases

- **Management consulting** — rapid due-diligence over large document sets
- **Legal / compliance** — query policy and regulatory documents
- **Research** — interrogate multiple papers or reports at once
- **Enterprise knowledge management** — internal document Q&A

---

## 🔮 Roadmap

- [ ] Multi-format support (DOCX, XLSX, web URLs)
- [ ] Persistent vector store (ChromaDB / Pinecone)
- [ ] Conversation memory (multi-turn Q&A)
- [ ] Deployment on Railway with live demo link
- [ ] Evaluation harness — precision@k on retrieved chunks

---

## 👨‍💻 Author

**Bhawani Lal**
MSc Advanced Computer Science with Data Science — University of Strathclyde, Glasgow

[![LinkedIn](https://img.shields.io/badge/LinkedIn-bhawani--lal-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/bhawani-lal)
[![GitHub](https://img.shields.io/badge/GitHub-Bhawani--Lal-181717?style=flat&logo=github)](https://github.com/Bhawani-Lal)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-gold?style=flat)](https://bhawani-portfolio.vercel.app)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
