from utils import FileUtils

file_path = "/home/hash/Desktop/ppt-png-conv/samplepptx.pptx"

print(f"number of pages calculate {FileUtils.get_pdf_page_count(file_path)}")