from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
out = StrOutputParser()

map_prompt = ChatPromptTemplate.from_template("""
You are a professional document summarizer.
Summarize this chunk clearly and concisely:

{chunk}
""")

reduce_prompt = ChatPromptTemplate.from_template("""
You are given partial summaries of a document:

{summaries}

Combine them into a final structured summary in 5-10 sentences.
""")

map_chain = map_prompt | llm | out
reduce_chain = reduce_prompt | llm | out


def summarize_text(text: str) -> str:
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunks = splitter.split_text(text)

    partials = []
    for chunk in chunks:
        partials.append(map_chain.invoke({"chunk": chunk}))

    final_summary = reduce_chain.invoke({"summaries": "\n\n".join(partials)})
    return final_summary