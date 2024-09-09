import os
from converter import PPTConverter
from utils import FileUtils

def process_files_in_directory(directory):
    """
    Process all PPTX files in the specified directory.

    Args:
        directory (str): The path to the directory containing PPTX files.

    Raises:
        Exception: For errors during file processing.
    """
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"The provided path {directory} is not a valid directory.")
        
        for filename in os.listdir(directory):
            if filename.lower().endswith('.pptx'):
                ppt_path = os.path.join(directory, filename)
                pdf_path = ppt_path.rsplit('.', 1)[0] + '.pdf'
                output_dir = os.path.join(directory, 'images', os.path.splitext(filename)[0])
                
                # Ensure output directory exists
                FileUtils.create_directory_if_not_exists(output_dir)
                
                # Initialize PPTConverter
                converter = PPTConverter(ppt_path, output_dir)
                
                # Convert PPTX to PDF
                converter.ppt_to_pdf()
                
                # Check if PDF was created
                if FileUtils.check_file_exists(pdf_path):
                    # Count pages in the PDF
                    page_count = FileUtils.get_pdf_page_count(pdf_path)
                    print(f"Number of pages in {pdf_path}: {page_count}")
                    
                    # Process PDF pages
                    converter.process_pdf_pages()
                else:
                    print(f"PDF file {pdf_path} does not exist.")
    except Exception as e:
        print(f"Error occurred while processing files: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert PPTX files to PNG images.")
    parser.add_argument("directory", help="Path to the directory containing PPTX files")
    args = parser.parse_args()
    
    process_files_in_directory(args.directory)
