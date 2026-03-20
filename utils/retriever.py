from pypdf import PdfReader


def load_pdf_text(file_path: str) -> list[str]:
    reader = PdfReader(file_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return pages


def get_context(query: str, pages: list[str]) -> str:
    query_words = query.lower().split()
    scored_pages = []

    for page in pages:
        page_lower = page.lower()
        match_count = sum(1 for word in query_words if word in page_lower)
        scored_pages.append((match_count, page))

    scored_pages.sort(key=lambda x: x[0], reverse=True)

    top_pages = [page for score, page in scored_pages if score > 0][:2]

    if top_pages:
        return "\n\n".join(top_pages)[:4000]

    return "\n\n".join(pages[:2])[:4000]