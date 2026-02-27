Project Summary

The Google Drive Document Summarizer is a production-oriented Generative AI web application built using Flask, LangChain v1 (LCEL), and OpenAI’s GPT-4o-mini model. The system automates document ingestion, large-text processing, and structured summarization directly from a specified Google Drive folder.

The application integrates Google OAuth 2.0 for secure authentication and uses the Google Drive REST API to retrieve files programmatically. It supports PDF, DOCX, and TXT formats. Text extraction is handled using pdfplumber for PDFs and python-docx for Word documents, enabling compatibility with standard enterprise document formats.

To efficiently process long documents within token constraints, the system implements a hierarchical Map-Reduce summarization pipeline using LangChain’s modern LCEL architecture. Documents are segmented using RecursiveCharacterTextSplitter from the langchain-text-splitters package. This chunking strategy ensures controlled context windows with configurable overlap, preserving semantic continuity.

The summarization workflow operates in two phases:

Map Phase: Each chunk is independently summarized using GPT-4o-mini.

Reduce Phase: Partial summaries are aggregated into a single coherent structured summary.

Using GPT-4o-mini provides a strong balance between performance, cost-efficiency, and summarization quality, making it suitable for scalable document analysis tasks.

The backend is implemented in Flask with a modular design:

drive_service.py handles OAuth authentication and Drive API interactions.

parser.py manages multi-format document extraction.

summarizer.py implements the LCEL-based Map-Reduce summarization chain.

app.py manages routing, request handling, and response rendering.

The frontend uses Bootstrap-based templating to display summaries in a structured tabular format. Additionally, the application supports CSV export functionality using Pandas, enabling reporting, auditing, or downstream data integration.

Key architectural characteristics include:

Secure API key management via environment variables

Persistent OAuth token storage (token.json)

Separation of concerns between ingestion, processing, and presentation layers

Token-aware chunking for large document handling

Scalable summarization strategy using GPT-4o-mini

Extensible architecture for future integration with databases or cloud deployment

This project demonstrates real-world GenAI engineering practices, including LLM integration, prompt design, hierarchical summarization, secure API usage, and full-stack Python web development. It is suitable for use cases such as enterprise report summarization, academic research condensation, legal document review, and automated knowledge extraction pipelines.

Overall, the system serves as a comprehensive example of applied Generative AI combining cloud APIs, modern LLM workflows, and web application architecture.
