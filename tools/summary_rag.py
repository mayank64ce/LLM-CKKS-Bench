import os
import json
from pathlib import Path
from typing import List, Optional

from langchain.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_chroma import Chroma


class SummaryRetriever:
    def __init__(
        self,
        summary_db_path: str,
        code_root: str,
        embedding_model: Optional[str] = "text-embedding-3-small",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        persist_directory: str = "./chroma_summary_store",
    ):
        """
        Initialize summary-based retriever.
        
        Args:
            summary_db_path: Path to JSON file with summaries
            code_root: Root directory for C++ files
            embedding_model: OpenAI embedding model name
            chunk_size: Split size for long summaries
            chunk_overlap: Overlap between summary chunks
        """
        self.summary_db_path = summary_db_path
        self.code_root = Path(code_root)
        self.embedding_model = embedding_model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Validate paths
        if not Path(summary_db_path).exists():
            raise FileNotFoundError(f"Summary DB not found at {summary_db_path}")
        if not self.code_root.exists():
            raise NotADirectoryError(f"Code root directory not found at {self.code_root}")

        # Load OpenAI API key
        if not os.environ.get("OPENAI_API_KEY"):
            import getpass
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter OpenAI API key: ")

        self.embeddings = OpenAIEmbeddings(model=self.embedding_model)
        self.vector_store = None

        self.persist_directory = persist_directory

        self._prepare_documents()
        self._create_vectorstore()

    def _prepare_documents(self):
        """Load and split summary documents with metadata"""
        loader = JSONLoader(
            file_path=self.summary_db_path,
            jq_schema=".summaries[] | {summary: .summary, file_path: .file_path}",
            content_key="summary",
            metadata_func=lambda record, metadata: {
                "file_path": record["file_path"]
            },
            text_content=True
        )
        
        raw_docs = loader.load()
        
        # Split documents while preserving metadata
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        self.splits = splitter.split_documents(raw_docs)

    def _create_vectorstore(self):
        """Create Chroma vector store with persistence"""
        if os.path.exists(self.persist_directory):
            # Load existing store
            self.vector_store = Chroma(
                embedding_function=self.embeddings,
                persist_directory=self.persist_directory
            )
        else:
            # Create new persistent store
            self.vector_store = Chroma.from_documents(
                documents=self.splits,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )

    def retrieve(self, query: str, k: int = 3) -> List[str]:
        """
        Retrieve full C++ file contents based on summary similarity.
        
        Args:
            query: Natural language query
            k: Number of files to retrieve
            
        Returns:
            List of file contents as strings
        """
        results = self.vector_store.similarity_search(query, k=k)
        return [self._load_code_file(doc.metadata["file_path"]) for doc in results]

    def _load_code_file(self, rel_path: str) -> str:
        """Load C++ file contents from relative path"""
        full_path = self.code_root / rel_path
        try:
            with open(full_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: File not found at {full_path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def get_summary_count(self) -> int:
        """Get total number of summary chunks"""
        return len(self.splits)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    retriever = SummaryRetriever(
        summary_db_path="../docs/summaries_db.json",
        code_root="../docs/openfhe-examples-cleaned",
        embedding_model="text-embedding-3-small"
    )

    query = "How to implement CKKS parameter setup in OpenFHE?"
    results = retriever.retrieve(query, k=1)

    for idx, content in enumerate(results):
        print(f"Result {idx+1}:\n{content[:300]}...\n{'-'*50}")