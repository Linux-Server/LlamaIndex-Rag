from docling.datamodel.base_models import InputFormat, ItemAndImageEnrichmentElement
from docling.datamodel.pipeline_options import (
    VlmConvertOptions,
    VlmPipelineOptions,
)
from docling_core.types.doc import ImageRefMode
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.models.stages.picture_description.picture_description_vlm_engine_model import (
    PictureDescriptionVlmEngineModel,
)
from docling.pipeline.vlm_pipeline import VlmPipeline

# Convert a public arXiv PDF; replace with a local path if preferred.
source = "https://arxiv.org/pdf/1706.03762"

vlm_options = VlmConvertOptions.from_preset("granite_docling")

pipeline_options = VlmPipelineOptions(
    vlm_options=vlm_options,
    generate_page_images=True,
    images_scale=2.0,  # higher-res page images give the describer better figure crops
)

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=pipeline_options,
        ),
    }
)

doc = converter.convert(source=source).document

# VlmPipeline's enrichment pipe is empty in docling 2.113, so
# do_picture_description is silently ignored there; run the description
# stage manually on the parsed document instead.
desc_options = pipeline_options.picture_description_options
desc_options.prompt = (
    "Describe this figure from a research paper in detail: what it depicts, "
    "its main components, and how they relate to each other."
)
desc_options.generation_config = {"max_new_tokens": 300, "do_sample": False}
desc_options.picture_area_threshold = 0.0  # describe every figure, even small ones

describer = PictureDescriptionVlmEngineModel(
    enabled=True,
    enable_remote_services=False,
    artifacts_path=None,
    options=desc_options,
    accelerator_options=pipeline_options.accelerator_options,
)

elements = [
    ItemAndImageEnrichmentElement(item=pic, image=img)
    for pic in doc.pictures
    if (img := pic.get_image(doc)) is not None
]

for pic in describer(doc=doc, element_batch=elements):
    print(f"--- {pic.self_ref} ---")
    print(pic.meta.description.text if pic.meta and pic.meta.description else "(no description)")
    print()

# PLACEHOLDER keeps the markdown image-free: each figure becomes an
# "<!-- image -->" marker followed by its generated description
# (include_annotations is on by default), and no PNG files are written.
doc.save_as_markdown(
    "/Users/sachin/Desktop/LlamaIndex-Rag/01_Loading/docs/attn_paper_vlm.md",
    image_mode=ImageRefMode.PLACEHOLDER,
)
