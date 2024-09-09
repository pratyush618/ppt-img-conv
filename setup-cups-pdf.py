import os
import subprocess
from datetime import datetime, timedelta

def is_package_installed(package_name):
    """
    Check if a specific package is installed on the system.

    Args:
        package_name (str): The name of the package to check.

    Returns:
        bool: True if the package is installed, False otherwise.
    """
    try:
        subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_packages():
    """
    Install CUPS and CUPS-PDF packages using apt-get.

    Raises:
        SystemExit: If there's an error during the installation process.
    """
    print("Installing CUPS and CUPS-PDF...")
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'cups', 'cups-pdf'], check=True)
        print("CUPS and CUPS-PDF installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        exit(1)

def configure_cups_pdf():
    """
    Configure CUPS-PDF settings by creating or updating the configuration file.

    Raises:
        SystemExit: If there's an error during configuration.
    """
    config_file = '/etc/cups/cups-pdf.conf'
    print("Configuring CUPS-PDF...")

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
        except Exception as e:
            print(f"Error configuring CUPS-PDF: {e}")
            exit(1)
    else:
        print(f"CUPS-PDF configuration file already exists at {config_file}. Skipping configuration.")

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
        exit(1)

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
        exit(1)

def needs_setup(timestamp_file, threshold_days=3):
    """
    Check if the setup needs to be performed based on the timestamp file.

    Args:
        timestamp_file (str): Path to the timestamp file.
        threshold_days (int): Number of days to check if setup is required (default is 3).

    Returns:
        bool: True if the setup needs to be performed, False otherwise.
    """
    if not os.path.exists(timestamp_file):
        return True

    with open(timestamp_file, 'r') as f:
        last_run = datetime.fromisoformat(f.read().strip())

    now = datetime.now()
    if now - last_run > timedelta(days=threshold_days):
        return True

    return False

def update_timestamp(timestamp_file):
    """
    Update the timestamp file with the current date and time.

    Args:
        timestamp_file (str): Path to the timestamp file.
    """
    with open(timestamp_file, 'w') as f:
        f.write(datetime.now().isoformat())

if __name__ == "__main__":
    timestamp_file = '/var/tmp/cups_setup_timestamp.txt'

    if needs_setup(timestamp_file):
        if not is_package_installed('cups-pdf'):
            install_packages()
        configure_cups_pdf()
        add_cups_pdf_printer()
        restart_cups()
        update_timestamp(timestamp_file)
    else:
        print("Setup already completed within the last 3 days. Skipping setup.")