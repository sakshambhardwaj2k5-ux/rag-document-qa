from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStoreManager:

    model_name = "sentence-transformers/all-mpnet-base-v2"

    def load_embedding_model(self,model_name):
        model_kwargs = {"device": "cpu"}
        encode_kwargs = {"normalize_embeddings": False}
        model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs,
        )
        return model
    def initialize_model(self):
        self.hf=self.load_embedding_model("sentence-transformers/all-mpnet-base-v2")

    def create_vector_store(self,collection_name,persist_directory):

        vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=self.hf,
        persist_directory=persist_directory
    )

        return vector_store

    def store_documents(self,vector_store, res_all_chunks):

        vector_store.add_documents(res_all_chunks)

        return vector_store