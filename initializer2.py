from llama_index.core import Settings

# Configure a global setting for our app so that the VectorStoreIndex and the QueryEngine can use these components by default.
Settings.llm = llm
Settings.embed_model = embed_model
Settings.prompt_helper = prompt_helper
Settings.node_parser = node_parser