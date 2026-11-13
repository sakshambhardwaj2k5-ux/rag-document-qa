from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

rag.ingest_documents("data/pdfs")

answer = rag.query_documents(
    "What is hydroponics?"
)

print(answer)