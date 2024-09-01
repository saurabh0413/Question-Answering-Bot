import fitz 

def load_pdf(file_content: bytes) -> str:
    document = fitz.open(stream=file_content, filetype="pdf")
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text