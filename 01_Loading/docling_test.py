
source = "/Users/sachin/Desktop/LlamaIndex-Rag/docs"  # file path or URL
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader(source).load_data()


from llama_index.core.node_parser import MarkdownNodeParser

parser = MarkdownNodeParser()

nodes = parser.get_nodes_from_documents(documents)


print(nodes[3].metadata)