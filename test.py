from src.ingestion.loaders.docling_loader import load_docling

docs = load_docling("data/Book.pdf")

print("Documents:", len(docs))

print()

print("Metadata")

print(docs[0].metadata)

print()

print("Content")

print(docs[0].page_content[:1500])