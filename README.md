# Books Vector Data Base Embedding Script

This script is used to create a vector database of books. It uses the Langchain library to load the books and the OpenAI API to embed them. The vector database is stored in a Chroma database.

The purpose of this project is to serve as a reference for how to create a vector database of documents, to be used for a chatbot. This is a reference project for MR Bookcamp students.

This is a work in progress and will be updated as we add more features to the project.


## Libraries and Their Uses

- **Langchain**: Framework for building applications with language models, used here for document loading and text splitting
- **OpenAI API**: Generates embeddings for the text chunks
- **Chroma**: Vector database for storing and querying embeddings
- **Unstructured**: Helps process unstructured data like markdown files
- **Tika**: Extracts text and metadata from various file formats
- **Dotenv**: Manages environment variables, particularly for the OpenAI API key
- **OS**: Handles file system operations
- **Shutil**: Manages file and directory operations, used for cleaning up the Chroma database

## Usage

1. Clone the repository
2. Install the requirements
3. Run the the following command to create the vector database:

```bash
python create_database.py
```
5. Optionally you can add more documents to books directory and run the script again.
6. Optionally you can clean the database by running:
```bash
python create_database.py --clean
```



