# naive_retriever.py

import os
from typing import List, Optional

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
# from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma

class NaiveRetriever:
    def __init__(
        self,
        path: str,
        persist_directory: str = "./chroma_store",
        embedding_model: Optional[str] = "text-embedding-3-large",
    ):
        """
        Initialize the retriever.
        Args:
            path (str): Path to the input .txt file.
            persist_directory (str): Path to persist the Chroma vector store.
            embedding_model (str): OpenAI embedding model to use.
        """
        self.path = path
        self.persist_directory = persist_directory
        self.embedding_model = embedding_model

        # Load OpenAI API key from env
        if not os.environ.get("OPENAI_API_KEY"):
            import getpass
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

        self.embeddings = OpenAIEmbeddings(model=self.embedding_model)
        self.vector_store = None

        self._prepare_documents()
        self._create_vectorstore()

    def _prepare_documents(self):
        loader = TextLoader(self.path)
        self.documents = loader.load()

        splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.C,
            chunk_size=512,
            chunk_overlap=128
        )
        self.splits = splitter.split_documents(self.documents)

    def _create_vectorstore(self):
        if os.path.exists(self.persist_directory):
            # Load existing vector store
            self.vector_store = Chroma(
                embedding_function=self.embeddings,
                persist_directory=self.persist_directory
            )
        else:
            # Create new vector store and persist it
            self.vector_store = Chroma.from_documents(
                documents=self.splits,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            # self.vector_store.persist()

    def retrieve(self, query: str, k: int = 3) -> str:
        """
        Perform similarity-based retrieval on the embedded documents.
        Args:
            query (str): The question or query string.
            k (int): Number of top matching chunks to return.
        Returns:
            str: Combined retrieved context snippets.
        """
        results = self.vector_store.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in results]).strip()

if __name__ == "__main__":
    retriever = NaiveRetriever(path="../docs/openfhe-examples-cleaned.txt")
    query = "How can I perform matrix multiplication of two ciphertexts?"
    context = retriever.retrieve(query)
    print(context)