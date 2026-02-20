from pathlib import Path


def ingest_knowledge_file(file_path: str) -> dict:
    path = Path(file_path)
    return {"status": "indexed", "source": str(path), "note": "Stub index; connect LangChain+Chroma in production."}


def query_knowledge(question: str) -> dict:
    return {
        "answer": (
            "RAG response placeholder. Connect LangChain retriever + Ollama Llama3 for grounded answers."
        ),
        "question": question,
    }
