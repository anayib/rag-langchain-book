# from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader  # Load documents from directory
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Split text into chunks
from langchain.schema import Document  # Document schema for Langchain
# from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings  # OpenAI embeddings for text
from langchain_community.vectorstores import Chroma  # Vector database for storing embeddings
import openai  # OpenAI API
from dotenv import load_dotenv  # Load environment variables from .env
import os  # OS operations
import shutil  # File operations like deleting database folder
import nltk
# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variables
openai.api_key = os.environ['OPENAI_API_KEY']

# Define paths
CHROMA_PATH = "chroma"  # Path to store Chroma database
DATA_PATH = "data/books"  # Path to source documents

def main():
    """Main function that runs the data store generation process"""
    generate_data_store()

def generate_data_store():
    """Pipeline for generating the vector data store"""
    documents = load_documents()  # Load documents from directory
    chunks = split_text(documents)  # Split documents into chunks
    save_to_chroma(chunks)  # Save chunks to Chroma database

def load_documents():
    """Load markdown documents from specified directory"""
    loader = DirectoryLoader(DATA_PATH, glob="*.md")  # Initialize loader for .md files
    documents = loader.load()  # Load all documents
    return documents

def split_text(documents: list[Document]):
    """Split documents into smaller chunks for processing"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,  # Maximum size of each chunk
        chunk_overlap=100,  # Overlap between chunks for context
        length_function=len,  # Function to calculate text length
        add_start_index=True,  # Track original position in source document
    )
    chunks = text_splitter.split_documents(documents)  # Split documents into chunks
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # Debug: Print sample chunk content and metadata
    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

def save_to_chroma(chunks: list[Document]):
    """Save processed chunks to Chroma vector database"""
    # Clear existing database if it exists
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create OpenAI embeddings with correct parameters
    # The newer version doesn't accept 'proxies' parameter
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.environ['OPENAI_API_KEY']
    )

    # Create new Chroma database from chunks
    db = Chroma.from_documents(
        chunks,  # Processed document chunks
        embeddings,  # OpenAI embedding function with proper config
        persist_directory=CHROMA_PATH  # Directory to store database
    )
    db.persist()  # Save database to disk
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

nltk.download('averaged_perceptron_tagger_eng')
# Entry point for script execution
if __name__ == "__main__":
    main()