📄 Google Drive Document Summarization System

Built with Flask • LangChain v1 (LCEL) • OpenAI GPT-4o-mini

🚀 Overview

The Google Drive Document Summarization System is a Generative AI–powered web application that automatically summarizes documents stored in a Google Drive folder.

The system:

Securely connects to Google Drive

Retrieves supported documents (PDF, DOCX, TXT)

Extracts text content

Generates structured summaries using GPT-4o-mini

Implements LangChain’s modern LCEL (LangChain Expression Language) framework

This project demonstrates real-world integration of LLMs + Cloud APIs + Web Development in a scalable architecture.

🏗️ System Architecture

The application follows a modular and scalable architecture with clear separation of responsibilities:

🔐 1. Google OAuth 2.0 Authentication

Secure access to user Google Drive

Token stored locally (token.json)

Credentials managed securely

☁️ 2. Google Drive API Integration

Fetches documents from a specified folder

Supports multi-file processing

📂 3. Document Parsing Layer

Handles different document formats:

PDF → pdfplumber

DOCX → python-docx

TXT → Native decoding

🧠 4. Summarization Engine (LangChain v1 LCEL)

Token-aware processing

Hierarchical Map-Reduce summarization

Uses OpenAI GPT-4o-mini

🌐 5. Flask Backend

Routing

Processing logic

API integration

Template rendering

🎨 6. Bootstrap Frontend

Clean summary display

Structured table format

CSV export functionality

🔄 How the Summarization Works

Large documents often exceed LLM token limits.
To handle this, the system implements a Map-Reduce strategy:

✂️ Step 1: Text Chunking

Uses RecursiveCharacterTextSplitter

Splits large documents into manageable chunks

Ensures:

Efficient token usage

Context preservation

Scalability for long documents

🗺️ Step 2: Map Phase

Each chunk is summarized independently

GPT-4o-mini processes chunks in parallel-style logic

🔁 Step 3: Reduce Phase

All partial summaries are merged

A final structured summary is generated

✅ This ensures:

Accuracy

Scalability

Efficient handling of long documents

🤖 Why GPT-4o-mini?

GPT-4o-mini was selected because:

✅ Strong summarization performance

✅ Cost-efficient compared to larger models

✅ Good structured text understanding

✅ Scalable for multi-document processing

Ideal for:

Academic research summarization

Enterprise report analysis

Automated knowledge extraction

🔐 Security & Configuration

Security best practices implemented:

API keys stored using environment variables (.env)

OAuth tokens stored securely in token.json

No hardcoded credentials in source code

Secure Google OAuth flow

✨ Key Features

🔐 Secure Google Drive integration

📄 Multi-format support (PDF, DOCX, TXT)

🧠 Token-aware chunk-based processing

🔄 Hierarchical Map-Reduce summarization

🌐 Clean and responsive UI

📊 CSV export functionality

🧩 Modular and extensible architecture

🛠️ Tech Stack
Layer	Technology
Backend	Flask
LLM Framework	LangChain v1 (LCEL)
Model	OpenAI GPT-4o-mini
Authentication	Google OAuth 2.0
Storage	Google Drive API
Parsing	pdfplumber, python-docx
Frontend	Bootstrap
Environment	Python, dotenv
📈 Scalability & Extensibility

The architecture separates:

Authentication

Document parsing

Summarization logic

Frontend rendering

This makes the system easy to extend for:

Database integration

Asynchronous/background processing

Batch document pipelines

Cloud deployment (Azure / GCP / AWS)

Multi-user access

Role-based authentication

🎯 Real-World Applications

Research paper summarization

Enterprise document analysis

Legal/financial report condensation

Automated knowledge extraction

Internal document intelligence systems

📌 Conclusion

The Google Drive Document Summarizer demonstrates a practical, end-to-end implementation of Generative AI integrated with cloud-based storage and web application development.
