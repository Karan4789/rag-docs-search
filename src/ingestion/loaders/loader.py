# src/ingestion/loaders/loader.py

import os

from langchain_docling import DoclingLoader


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

    loader = DoclingLoader(
        file_path=file_path
    )

    docs = loader.load()

    return docs