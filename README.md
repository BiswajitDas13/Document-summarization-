Project Summary
Google Drive Document Summarization System
Built with Flask, LangChain (v1 LCEL), and OpenAI GPT-4o-mini

Overview:
This project is a Generative AI–powered web application designed to automatically summarize documents stored in a Google Drive folder. The system securely connects to Google Drive, retrieves supported documents (PDF, DOCX, TXT), extracts their text content, and generates structured summaries using OpenAI’s GPT-4o-mini model through LangChain’s modern LCEL framework.
The goal of this project is to demonstrate real-world integration of Large Language Models (LLMs) with cloud APIs and web application development.

System Architecture:
The application follows a modular architecture with clear separation of responsibilities:
Google OAuth 2.0 Authentication
Ensures secure access to user Drive data.
Google Drive API Integration
Retrieves files from a specified folder.
Document Parsing Layer
pdfplumber for PDF extraction
python-docx for DOCX processing
Native decoding for TXT files
Summarization Engine (LangChain v1 LCEL)
Implements a hierarchical Map-Reduce summarization strategy.
Flask Backend
Handles routing, processing logic, and UI rendering.
Bootstrap Frontend
Displays summaries in a structured table format.

How the Summarization Works:
Large documents often exceed LLM token limits. To solve this, the system uses a two-step Map-Reduce approach:
Text Chunking:
The document text is split into smaller chunks using RecursiveCharacterTextSplitter.
This ensures:
Efficient token usage
Context preservation
Scalability for long documents
Map Phase:
Each chunk is summarized independently using GPT-4o-mini.
Reduce Phase:
All partial summaries are combined into a final structured summary.
This approach ensures accuracy, scalability, and better handling of long documents.
Why GPT-4o-mini?
GPT-4o-mini was selected because:
It provides strong summarization quality
It is cost-efficient compared to larger models
It performs well for structured text analysis
It supports scalable processing for multiple documents
This makes it ideal for document summarization tasks in academic and enterprise settings.
Security & Configuration:
API keys are stored securely using environment variables (.env).
OAuth tokens are stored locally in token.json after first authorization.
Sensitive credentials are not exposed in source code.

Key Features:
Secure Google Drive integration
Multi-format document support (PDF, DOCX, TXT)
Token-aware chunk-based processing
Hierarchical summarization
Clean UI for summary display
CSV export functionality
Modular and extensible architecture

Conclusion:
The Google Drive Document Summarizer project presents a practical implementation of Generative AI integrated with cloud-based document storage and web application development. The system successfully demonstrates how large language models can be applied to automate document analysis and structured summarization in a scalable and secure manner.
By combining Google OAuth 2.0 authentication, Google Drive API integration, and OpenAI’s GPT-4o-mini model through LangChain v1 LCEL, the application provides an end-to-end pipeline that retrieves documents, extracts textual content, processes large inputs efficiently using chunk-based Map-Reduce summarization, and delivers concise, structured summaries through a user-friendly web interface.
The architecture ensures modularity and scalability by separating authentication, document parsing, summarization logic, and frontend rendering into independent components. This design makes the system easy to maintain, extend, and adapt for future enhancements such as database integration, asynchronous processing, or cloud deployment.
The use of token-aware chunking strategies allows the system to handle large documents effectively without exceeding model limitations, demonstrating an understanding of real-world LLM constraints and optimization techniques. Additionally, secure credential handling and environment-based configuration reflect good software engineering practices.
Overall, this project illustrates the practical application of Generative AI technologies in solving real-world problems such as report summarization, research document condensation, and automated knowledge extraction. It highlights how modern AI models can be integrated with APIs and web frameworks to build intelligent, scalable, and user-centric systems.
