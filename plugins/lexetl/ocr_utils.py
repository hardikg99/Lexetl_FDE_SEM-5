# lexetl/ocr_utils.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import pdfplumber

def pdf_has_text(pdf_path: str) -> bool:
    doc = fitz.open(pdf_path)
    for page in doc:
        text = page.get_text().strip()
        if text:
            return True
    return False

def pdf_to_text(pdf_path: str) -> str:
    # Try text extraction first, fall back to OCR if empty
    try:
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
        if text.strip():
            return text
    except Exception:
        pass

    # Fallback: use pdfplumber + pytesseract on images
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text and page_text.strip():
                text += page_text + "\n"
            else:
                # rasterize page and OCR
                im = page.to_image(resolution=300).original
                ocr_text = pytesseract.image_to_string(Image.fromarray(im))
                text += ocr_text + "\n"
    return text
