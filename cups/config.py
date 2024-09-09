import os

# Define a hidden directory for storing the timestamp file
HIDDEN_DIR = os.path.expanduser("~/.cups_setup")
TIMESTAMP_FILE = os.path.join(HIDDEN_DIR, 'setup_timestamp.txt')

def ensure_hidden_dir_exists():
    """
    Ensure that the hidden directory for configuration files exists.
    
    This function creates the hidden directory if it does not already exist.
    """
    try:
        if not os.path.exists(HIDDEN_DIR):
            os.makedirs(HIDDEN_DIR)
    except OSError as e:
        print(f"Error creating hidden directory: {e}")
        raise

def get_timestamp_file():
    """
    Get the path to the timestamp file.
    
    This function ensures that the hidden directory exists and returns the 
    path to the timestamp file used for tracking setup completion.

    Returns:
        str: The path to the timestamp file.
    """
    try:
        ensure_hidden_dir_exists()
    except Exception as e:
        print(f"Error ensuring hidden directory: {e}")
        raise
    return TIMESTAMP_FILE
