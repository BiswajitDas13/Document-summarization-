Project Summary

The Google Drive Document Summarizer is a full-stack Generative AI system engineered to automate large-scale document ingestion and structured summarization using OpenAI’s GPT-4o-mini model. The application integrates Google Drive APIs, OAuth 2.0 authentication, and LangChain v1’s LCEL framework to build a scalable, modular, and token-aware summarization pipeline.

The system securely authenticates users via Google OAuth 2.0 and programmatically retrieves documents from a specified Google Drive folder using the Drive REST API. It supports multi-format document processing (PDF, DOCX, TXT), with format-specific parsing handled through pdfplumber and python-docx. This ensures robust extraction of textual content from heterogeneous document types commonly used in enterprise workflows.

Given the token limitations inherent in large language models, the system implements a hierarchical Map-Reduce summarization strategy using LangChain’s modern LCEL (LangChain Expression Language) architecture. The workflow consists of:

Preprocessing & Segmentation
Documents are segmented using RecursiveCharacterTextSplitter with controlled chunk size and overlap. This ensures contextual continuity while maintaining token efficiency.

Map Phase (Chunk-Level Summarization)
Each chunk is independently summarized using GPT-4o-mini, enabling parallelizable processing and improved scalability.

Reduce Phase (Summary Aggregation)
Intermediate summaries are recursively combined into a final structured, coherent summary, preserving key insights while minimizing redundancy.

GPT-4o-mini was selected to optimize performance-to-cost ratio while maintaining strong summarization quality, making the system viable for high-volume document processing scenarios.

The application architecture follows a clean separation-of-concerns model:

drive_service.py manages authentication, token persistence, and API interactions.

parser.py handles document format detection and text extraction.

summarizer.py encapsulates the LCEL-based LLM workflow.

app.py orchestrates request handling, response rendering, and data flow.

The backend is implemented in Flask, offering a lightweight yet extensible framework suitable for production deployment with WSGI servers (e.g., Gunicorn). The frontend leverages Bootstrap-based templating for structured data visualization and integrates CSV export functionality via Pandas for downstream analytics.

Security and configuration best practices are applied through environment variable management (.env), secure credential storage, and OAuth token reuse (token.json). The architecture is extensible and can be adapted for asynchronous processing, database-backed caching, containerized deployment, or integration with enterprise data pipelines.

This project demonstrates applied GenAI engineering principles, including LLM workflow orchestration, token-aware document processing, cloud API integration, and modular web application design. It serves as a scalable foundation for enterprise use cases such as automated report generation, research summarization, compliance document analysis, and intelligent knowledge extraction systems.
