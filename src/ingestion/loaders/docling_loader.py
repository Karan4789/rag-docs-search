    # src/ingestion/loaders/docling_loader.py

import os
from langchain_docling import DoclingLoader, loader

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import (
    DocumentConverter,
    PdfFormatOption
)
# from docling.backend.docling_parse_v2_backend import DoclingParseDocumentBackend

def load_docling(file_path):
        """
        Load documents using Docling.

        Supports:
            • PDF
            • DOCX
            • PPTX
            • XLSX
            • CSV
            • HTML
        """

        print(
            f"📄 Using DoclingLoader for "
            f"{os.path.basename(file_path)}..."
        )

        pipeline_options = PdfPipelineOptions()
        pipeline_options.allow_external_plugins = True
        pipeline_options.do_ocr = False
        pipeline_options.do_table_structure = False

        converter = DocumentConverter(
        format_options={
            InputFormat.PDF:
                PdfFormatOption(
                    pipeline_options=pipeline_options
                )
        }
    )

        loader = DoclingLoader(
        file_path=file_path,
        converter=converter
    )

        return loader.load()