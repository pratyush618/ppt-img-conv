import os
from datetime import datetime, timedelta

def needs_setup(timestamp_file, threshold_days=3):
    """
    Check if the setup needs to be performed based on the timestamp file.

    Args:
        timestamp_file (str): Path to the timestamp file.
        threshold_days (int): Number of days to check if setup is required 
                              (default is 3).

    Returns:
        bool: True if the setup needs to be performed, False otherwise.
    """
    try:
        if not os.path.exists(timestamp_file):
            return True

        with open(timestamp_file, 'r') as f:
            last_run = datetime.fromisoformat(f.read().strip())

        now = datetime.now()
        return now - last_run > timedelta(days=threshold_days)
    except (OSError, ValueError) as e:
        print(f"Error checking setup needs: {e}")
        raise

def update_timestamp(timestamp_file):
    """
    Update the timestamp file with the current date and time.

    Args:
        timestamp_file (str): Path to the timestamp file.
    """
    try:
        with open(timestamp_file, 'w') as f:
            f.write(datetime.now().isoformat())
    except OSError as e:
        print(f"Error updating timestamp file: {e}")
        raise
