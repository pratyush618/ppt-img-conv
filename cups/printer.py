import os
import subprocess

def configure_cups_pdf():
    """
    Configure CUPS-PDF settings by creating or updating the configuration file.

    Raises:
        SystemExit: If there's an error during configuration.
    """
    config_file = '/etc/cups/cups-pdf.conf'
    print("Configuring CUPS-PDF...")

    try:
        if not os.path.exists(config_file):
            print(f"Configuration file {config_file} does not exist. Creating new one.")
            try:
                with open(config_file, 'w') as f:
                    f.write("""
# CUPS-PDF configuration file
# Output directory for PDF files
Outfile /home/yourusername/PDF
# Other options can be set here
""")
                subprocess.run(['sudo', 'chown', 'root:lp', config_file], check=True)
                subprocess.run(['sudo', 'chmod', '644', config_file], check=True)
                print("CUPS-PDF configured successfully.")
            except (OSError, subprocess.CalledProcessError) as e:
                print(f"Error creating or configuring CUPS-PDF file: {e}")
                raise
        else:
            print(f"CUPS-PDF configuration file already exists at {config_file}. Skipping configuration.")
    except Exception as e:
        print(f"Error during CUPS-PDF configuration: {e}")
        raise

def add_cups_pdf_printer():
    """
    Add the CUPS-PDF printer to the system.

    Raises:
        SystemExit: If there's an error adding the printer.
    """
    print("Adding CUPS-PDF printer...")
    try:
        # Check if the printer already exists
        printers = subprocess.check_output(['lpstat', '-p'], text=True)
        if 'CUPS-PDF' in printers:
            print("CUPS-PDF printer already exists. Skipping addition.")
        else:
            subprocess.run(['sudo', 'lpadmin', '-p', 'CUPS-PDF', '-E', '-v', 'cups-pdf:', '-P', '/usr/share/ppd/cups-pdf/0ppd.pdf'], check=True)
            print("CUPS-PDF printer added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding CUPS-PDF printer: {e}")
        raise

def restart_cups():
    """
    Restart the CUPS service to apply changes.

    Raises:
        SystemExit: If there's an error restarting the service.
    """
    print("Restarting CUPS service...")
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', 'cups'], check=True)
        print("CUPS service restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting CUPS service: {e}")
        raise