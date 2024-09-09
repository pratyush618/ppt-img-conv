import os
import subprocess

from multiprocessing import Pool, cpu_count
from pdf2image import convert_from_path
from utils import FileUtils

class PPTConverter:
    def __init__(self, ppt_path, output_dir, num_processes=None):
        """
        Initialize PPTConverter with paths and multiprocessing parameters.

        Args:
            ppt_path (str): The path to the PowerPoint file.
            output_dir (str): The directory where PNG images will be saved.
            num_processes (int, optional): The number of processes to use for multiprocessing. Defaults to None.
        """
        self.ppt_path = ppt_path
        self.output_dir = output_dir
        self.num_processes = num_processes or cpu_count()
        self.pdf_path = ppt_path.rsplit('.', 1)[0] + '.pdf'

    def ppt_to_pdf(self):
        """
        Convert PowerPoint file (.pptx) to PDF using LibreOffice.

        Raises:
            subprocess.CalledProcessError: If the conversion process fails.
            Exception: For unexpected errors during the conversion.
        """
        try:
            command = ['soffice', '--headless', '--convert-to', 'pdf', self.ppt_path, '--outdir', os.path.dirname(self.pdf_path)]
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while converting PPT to PDF: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    @staticmethod
    def get_padded_filename(base_name, number, total_digits):
        """
        Generate a filename with zero-padded numbers.

        Args:
            base_name (str): The base name for the file.
            number (int): The number to be padded and included in the filename.
            total_digits (int): The total number of digits for padding.

        Returns:
            str: The padded filename.
        """
        return f"{base_name}-{number:0{total_digits}}.png"

    def convert_page_to_png(self, page_info):
        """
        Convert a single page of the PDF to a PNG image.

        Args:
            page_info (tuple): A tuple containing the PDF path, page number, and output directory.

        Raises:
            Exception: For errors during the image conversion process.
        """
        pdf_path, page_number, output_dir = page_info
        try:
            images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
            image_filename = self.get_padded_filename("slide", page_number, 4)  # Assuming 4-digit padding
            image_path = os.path.join(output_dir, image_filename)
            images[0].save(image_path, 'JPEG')
            print(f"Saved {image_path}")
        except Exception as e:
            print(f"Error occurred while converting page {page_number} to PNG: {e}")
            raise

    def process_pdf_pages(self):
        """
        Convert all pages of a PDF to PNG images, using multiprocessing if necessary.

        Raises:
            Exception: For errors during the page processing.
        """
        try:
            # Get the number of pages
            num_pages = FileUtils.get_pdf_page_count(self.pdf_path)
            
            # Prepare data for processing
            page_infos = [(self.pdf_path, i + 1, self.output_dir) for i in range(num_pages)]

            if num_pages > 100:
                # Use multiprocessing for a large number of pages
                with Pool(processes=self.num_processes) as pool:
                    pool.map(self.convert_page_to_png, page_infos)
            else:
                # Use a single process for a smaller number of pages
                for page_info in page_infos:
                    self.convert_page_to_png(page_info)
        except Exception as e:
            print(f"Error occurred while processing PDF pages: {e}")
            raise



if __name__ == "__main__":
    import time
    st = time.time()
    conv = PPTConverter("/home/hash/Desktop/ppt-png-conv/filepath/Learning_Python.pdf", "images/")
    conv.process_pdf_pages()
    print(f"total time taken: {time.time() - st}")