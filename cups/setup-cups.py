from config import get_timestamp_file
from utils import needs_setup, update_timestamp
from installer import is_package_installed, install_packages
from printer import configure_cups_pdf, add_cups_pdf_printer, restart_cups

def main():
    """
    Main function to run the setup script.

    This function checks if the setup needs to be performed by evaluating the 
    timestamp file. If the setup is required, it installs the necessary 
    packages, configures CUPS-PDF, adds the printer, and restarts the CUPS 
    service. It then updates the timestamp file to indicate the setup 
    completion.
    """
    timestamp_file = get_timestamp_file()

    try:
        if needs_setup(timestamp_file):
            if not is_package_installed('cups-pdf'):
                install_packages()
            configure_cups_pdf()
            add_cups_pdf_printer()
            restart_cups()
            update_timestamp(timestamp_file)
        else:
            print("Setup already completed within the last 3 days. Skipping setup.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
