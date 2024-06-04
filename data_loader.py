from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Load data from a specified directory and file
document = SimpleDirectoryReader(input_files=['/path/to/data.txt']).load_data()

# Process data (chunking, embedding, indexing) and store them
index = VectorStoreIndex.from_documents(document)
