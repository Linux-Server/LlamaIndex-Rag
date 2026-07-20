from docling.document_converter import DocumentConverter

source_file = "https://arxiv.org/pdf/1706.03762"

converter = DocumentConverter()

doc = converter.convert(source_file).document

print(doc)