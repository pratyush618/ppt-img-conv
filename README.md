# ppt-img-conv
Python curated script to convert large ppts files to images efficiently


# CUPS-PDF Setup and Print Automation

This project automates the setup and configuration of CUPS (Common Unix Printing System) and CUPS-PDF (a virtual PDF printer) on a Unix-like system. It also provides functionality to convert files, such as PowerPoint presentations, to PDFs using CUPS.

## Project Structure

The project consists of the following files:




### File Descriptions

- **`config.py`**: Contains configuration constants and functions for managing hidden directory paths and timestamp files.
- **`installer.py`**: Handles installation of necessary packages.
- **`printer.py`**: Manages configuration and setup of the CUPS-PDF printer.
- **`setup_cups.py`**: Main script that orchestrates the setup and configuration of CUPS-PDF.
- **`utils.py`**: Provides utility functions for checking setup needs and updating timestamps.
- **`__init__.py`**: Makes the directory a Python package (can be empty or contain package-level docstring).

## Installation

### Prerequisites

- Python 3.11 or later
- sudo privileges for installing packages and configuring system settings
- LibreOffice (for converting PPTX to PDF)
- Python libraries: `pdf2image`, `PyMuPDF`, `pytesseract` (for OCR if needed)

### Install Dependencies

Install the required Python package using pip:


### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 
