import os
import fitz
import shutil

def capture_pdf(pdf_file_path, out_folder):
    pdf_document = fitz.open(pdf_file_path)
    total_page = len(pdf_document)
    for i in range(total_page):
        page_number = i
        page = pdf_document.load_page(page_number)
        image = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        image_file = f"{out_folder}/docx_{pdf_file_path.split('/')[-1].split('.')[0]}_page_{page_number}.jpg"
        image.save(image_file)
    print(f"Images Saved...{image_file}")

def create_dir(path):
    try:
        os.makedirs(path, exist_ok=False)
    except:
        pass

def delete_dir(path):
    try:
        shutil.rmtree(path)
    except:
        pass