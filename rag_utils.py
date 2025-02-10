from langchain_core.documents import Document

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import MarkdownTextSplitter, RecursiveCharacterTextSplitter


def split_markdown(md: str) -> list[str]:
    spl = MarkdownTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
    )
    return spl.split_text(md)


def split_string(text: str) -> list[str]:
    spl = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
    )
    return spl.split_text(text)

class RAGManager:
    def __init__(self, embeddings_model: str = 'mxbai-embed-large'):
        self.embeddings = OpenAIEmbeddings(
            model=embeddings_model,
            base_url='http://localhost:11434/v1'
        )
        self.vector_store = Chroma(embedding_function=self.embeddings)

    def store_markdown(self, md: str, url: str = ''):
        """
        Stores a given markdown string in the knowledge base
        so you can always retrieve it at any time when you need it.
        Providing the source as url would be helpful.
        """
        chunks = split_markdown(md)
        self.vector_store.add_texts(chunks, [{'source': url}])

    def retrieve_from_query(self, query: str) -> list[Document]:
        """
        Query our knowledge base to get accurate information which you can rely upon.
        """
        return self.vector_store.similarity_search(query)