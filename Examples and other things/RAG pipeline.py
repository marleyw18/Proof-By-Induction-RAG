from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# loading files. specifically txt
from langchain_community.document_loaders import TextLoader
# Fill with actual file later on // loader = TextLoader('data/my_document.txt')
documents = loader.load()

# chunking text
from langchain.text_splitter import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
document_chunks = splitter.split_documents(documents)

# embeddings
from langchain_openai.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# create vector store
from langchain_community.vectorstores import FAISS
vector_store = FAISS.from_documents(document_chunks, embeddings)

# set up retriever
retriever = vector_store.as_retriever(
	 search_type="similarity",
	 search_kwargs={"k": 5}
	)