class QueryAndRetrieval:

    def search_similar_documents(self, vector_store, query, k=2):
        results = vector_store.similarity_search(query=query, k=k)
        return results

    def create_context(self,search_results):
        context=''
        for doc in search_results:
            context += doc.page_content + '\n'
        return context

    def create_prompt(self,context, query1):
        prompt = f"Context: {context}\n\nQuestion: {query1}\nAnswer:"
        return prompt

    