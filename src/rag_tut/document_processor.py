from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentProcessor:

    def load_pdf(self, file_path):
        all_documents = []
        folder=Path(file_path)
        if not folder.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not folder.is_dir():
            raise ValueError(f"Provided path is not a directory: {file_path}")

        files = list(folder.glob("*.pdf"))
        if not files:
            print(f"No PDF files found in {file_path}")
            return all_documents

        for file in files:
            try:
                loader = PyPDFLoader(str(file))
                documents = loader.load()
                print(f"Loaded {len(documents)} documents from {file}")
                all_documents.extend(documents)
            except Exception as e:
                print(f"Error loading {file}: {e}")
            
            print(f"Total documents loaded so far: {len(all_documents)}")
        return all_documents

    from langchain_text_splitters import RecursiveCharacterTextSplitter

    def split_documents(self,documents):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
        all_chunks = text_splitter.split_documents(documents)
        return all_chunks