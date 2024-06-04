from llama_index.core.indices.prompt_helper import PromptHelper
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
# Initialize PromptHelper and SentenceSplitter
prompt_helper = PromptHelper(context_window=2048)
node_parser = SentenceSplitter(chunk_size=300, chunk_overlap=20)

# Update Settings with helpers
Settings.prompt_helper = prompt_helper
Settings.node_parser = node_parser
