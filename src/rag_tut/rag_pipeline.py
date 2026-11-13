
from src.document_processor import DocumentProcessor
from src.vector_store_manager import VectorStoreManager
from src.query_retrieval import QueryAndRetrieval
from src.llm_service import LLMService

class RAGPipeline:
    def __init__(self):

        self.document_processor = DocumentProcessor()

        self.vector_store_manager = VectorStoreManager()

        self.query_retrieval = QueryAndRetrieval()

        self.llm_service = LLMService()

        self.llm_service.initialize_model()

        self.vector_store = None


    def ingest_documents(self,file_path):
        documents = self.document_processor.load_pdf(file_path)

        chunks = self.document_processor.split_documents(documents)

        self.vector_store_manager.initialize_model()

        self.vector_store = self.vector_store_manager.create_vector_store(
        collection_name="Collection",
        persist_directory="./chroma_db"
        )

        self.vector_store_manager.store_documents(
        self.vector_store,
        chunks
    )

    def query_documents(self, query, k=2):

        if self.vector_store is None:
            raise ValueError("Please ingest documents before asking questions.")

        results = self.query_retrieval.search_similar_documents(
            self.vector_store,
            query,
            k
        )

        context = self.query_retrieval.create_context(results)

        prompt = self.query_retrieval.create_prompt(context, query)

        answer = self.llm_service.generate_response(prompt)

        return answer

