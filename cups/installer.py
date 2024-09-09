import subprocess

def is_package_installed(package_name):
    """
    Check if a package is installed.

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
    Install CUPS and CUPS-PDF packages.

    Raises:
        SystemExit: If there's an error during installation.
    """
    print("Installing CUPS and CUPS-PDF...")
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'cups', 'cups-pdf'], check=True)
        print("CUPS and CUPS-PDF installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        raise
