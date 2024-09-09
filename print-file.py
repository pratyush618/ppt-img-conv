import subprocess
import sys

def print_file(file_path):
    """Send the file to the CUPS-PDF printer."""
    print("Sending file to CUPS-PDF printer...")
    try:
        subprocess.run(['lp', '-d', 'CUPS-PDF', file_path], check=True)
        print(f"File '{file_path}' sent to CUPS-PDF printer.")
    except subprocess.CalledProcessError as e:
        print(f"Error printing file: {e}")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print_file(file_path)