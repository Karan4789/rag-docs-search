import pymupdf4llm

pages = pymupdf4llm.to_markdown(
    "data/Book.pdf",
    page_chunks=True
)

print(type(pages))
print(len(pages))

print()

print(pages[0].keys())