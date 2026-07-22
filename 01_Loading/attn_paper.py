# Since the data is a pdf we use docstring
# Paper is : Attention all you need( arxiv)
from docling.document_converter import DocumentConverter


url ="https://arxiv.org/pdf/1706.03762"

converter = DocumentConverter()

res = converter.convert(url).document

res.save_as_markdown("/Users/sachin/Desktop/LlamaIndex-Rag/01_Loading/docs/attn_paper.md")
