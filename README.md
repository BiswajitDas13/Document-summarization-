# 📄 Google Drive Document Summarization System

**Built with Flask • LangChain v1 (LCEL) • OpenAI GPT-4o-mini**

---

## 🚀 Overview

The Google Drive Document Summarization System is a Generative AI–powered web application designed to automatically summarize documents stored in a Google Drive folder.

The system securely connects to Google Drive, retrieves supported documents (PDF, DOCX, TXT), extracts textual content, and generates structured summaries using OpenAI GPT-4o-mini through LangChain’s LCEL (LangChain Expression Language) framework.

This project demonstrates real-world integration of Large Language Models (LLMs) with cloud APIs and scalable web application development.

---

## 🏗️ System Architecture

The application follows a modular and scalable architecture with clear separation of responsibilities.

### 1. Google OAuth 2.0 Authentication
- Ensures secure access to user Google Drive data
- OAuth tokens stored locally after first authorization

### 2. Google Drive API Integration
- Retrieves files from a specified folder
- Supports multi-document processing

### 3. Document Parsing Layer
- **PDF** → pdfplumber
- **DOCX** → python-docx
- **TXT** → Native decoding

### 4. Summarization Engine (LangChain v1 LCEL)
- Hierarchical Map-Reduce summarization
- Token-aware chunking strategy
- Powered by GPT-4o-mini

### 5. Flask Backend
- Routing
- Business logic
- Document processing
- UI rendering

### 6. Bootstrap Frontend
- Structured summary display
- Clean UI
- CSV export functionality

---

## 🔄 How the Summarization Works

Large documents often exceed LLM token limits.  
To solve this, the system uses a two-step Map-Reduce strategy.

### Step 1: Text Chunking
- Uses RecursiveCharacterTextSplitter
- Splits large documents into manageable chunks
- Ensures efficient token usage and context preservation

### Step 2: Map Phase
- Each chunk is summarized independently using GPT-4o-mini
- Enables controlled processing of large inputs

### Step 3: Reduce Phase
- Partial summaries are merged
- Generates a final structured summary

This ensures scalability, accuracy, and effective long-document handling.

---

## 🤖 Why GPT-4o-mini?

- Strong summarization performance
- Cost-efficient compared to larger models
- Performs well for structured text analysis
- Supports scalable multi-document processing

Ideal for academic, enterprise, and automated knowledge extraction use cases.

---

## 🔐 Security & Configuration

- API keys stored using environment variables (.env)
- OAuth tokens stored in token.json
- No hardcoded credentials in source code
- Secure Google OAuth flow

---

## ✨ Key Features

- Secure Google Drive integration
- Multi-format support (PDF, DOCX, TXT)
- Token-aware chunk-based processing
- Hierarchical Map-Reduce summarization
- Clean and responsive UI
- CSV export functionality
- Modular and extensible architecture

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Flask |
| LLM Framework | LangChain v1 (LCEL) |
| Model | OpenAI GPT-4o-mini |
| Authentication | Google OAuth 2.0 |
| Cloud Storage | Google Drive API |
| Document Parsing | pdfplumber, python-docx |
| Frontend | Bootstrap |
| Environment | Python, dotenv |

---

## 📈 Scalability & Extensibility

The system separates:
- Authentication
- Document parsing
- Summarization logic
- Frontend rendering

This makes it easy to extend with:
- Database integration
- Asynchronous processing
- Cloud deployment
- Multi-user support
- Role-based authentication

---

## 📌 Conclusion

The Google Drive Document Summarizer demonstrates a practical, end-to-end implementation of Generative AI integrated with cloud storage and web application development.

By combining Google OAuth 2.0, Google Drive API, LangChain v1 LCEL, GPT-4o-mini, and Flask, the system delivers secure document retrieval, efficient large-text handling, structured summarization, and scalable architecture.

This project highlights how modern LLM systems can be integrated into real-world applications using modular design, secure configuration, and token-aware processing strategies.
