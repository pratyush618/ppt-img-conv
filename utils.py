import fitz
import os

class FileUtils:
    @staticmethod
    def get_pdf_page_count(pdf_path):
        """
        Get the number of pages in a PDF using PyMuPDF.

        Args:
            pdf_path (str): The path to the PDF file.

        Returns:
            int: The number of pages in the PDF.

        Raises:
            Exception: For errors during the PDF page count process.
        """
        try:
            pdf_document = fitz.open(pdf_path)
            num_pages = pdf_document.page_count
            pdf_document.close()
            return num_pages
        except Exception as e:
            print(f"Error occurred while counting pages: {e}")
            raise

    @staticmethod
    def check_file_exists(file_path):
        """
        Check if a file exists.

        Args:
            file_path (str): The path to the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(file_path)

    @staticmethod
    def create_directory_if_not_exists(directory):
        """
        Create a directory if it does not already exist.

        Args:
            directory (str): The path to the directory to create.

        Raises:
            Exception: For errors during directory creation.
        """
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except Exception as e:
            print(f"Error occurred while creating directory {directory}: {e}")
            raise