### Loading

 - Loading = getting the document.
 - Parsing = understanding and extracting its content.
- They are not the same, although many libraries combine them into a single API call, which can make them seem like one step.

| Stage         | Responsibility                           | Example Tool                            |
| ------------- | ---------------------------------------- | --------------------------------------- |
| **Loading**   | Access the file or data source           | Local filesystem, S3, Google Drive      |
| **Parsing**   | Convert the file into structured content | Docling, Unstructured, LlamaParse       |
| **Cleaning**  | Remove noise (headers, footers, etc.)    | Custom code                             |
| **Chunking**  | Split into retrieval units               | LlamaIndex `SemanticSplitterNodeParser` |
| **Embedding** | Convert chunks to vectors                | BGE, Qwen Embedding                     |
| **Storage**   | Save vectors and metadata                | Qdrant, Milvus                          |


## We can use LlamaParse(cloud charges) or Docling(local) or Unstructured(local)