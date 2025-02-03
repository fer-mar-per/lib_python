u"""
2025/02/03 - Fernando Martin Perucki @ Perucki Lab
This script was created for the following goal:
- Look for all the files (not including folders) under the specified directory.
- Obtain all the dates those files were created. As the goal was for photos and videos, it will first
  try to get the 'Date Taken' from EXIF metadata if available. If it can't find it, it will then try to
  get file creation date (or last modified date as fallback).
- After getting the dates from the files, it will create subdirectories with the name format YYYY-MM-DD
  matching those dates.
- Finally, it will move the files to their respective subdirectories.

Other notes:
- This script supposedly works for Windows, Mac and Linux, but it was only tested on Windows 11.
- Inside the target directory, a log file will be also generated, to store each and every step of the process.
"""

import os
import shutil
import sys
import platform
import logging
from pathlib import Path
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

SCRIPT_NAME = "filesOrganizer"

def setup_logging(directory):
    """Sets up a unique log file in the target directory with a timestamped filename."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = directory / f"{timestamp}_{SCRIPT_NAME}.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return log_file

def get_photo_date_taken(photo_path):
    """Extract 'Date Taken' from EXIF metadata if available."""
    try:
        image = Image.open(photo_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":  # EXIF Date Taken
                    logging.info(f"Date Taken found for {photo_path}: {value}")
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        logging.error(f"Error reading EXIF data for {photo_path}: {e}")
    return None

def get_file_creation_date(file_path):
    """Get file creation date (or last modified date as fallback)."""
    try:
        if platform.system() == "Windows":
            creation_date = datetime.fromtimestamp(os.path.getctime(file_path))  # Windows Creation Date
        elif platform.system() == "Darwin":  # macOS
            creation_date = datetime.fromtimestamp(os.stat(file_path).st_birthtime)  # macOS Birth Time
        else:
            creation_date = datetime.fromtimestamp(os.stat(file_path).st_mtime)  # Linux Fallback
        logging.info(f"Using Creation Date for {file_path}: {creation_date}")
        return creation_date
    except Exception as e:
        logging.error(f"Error getting creation date for {file_path}: {e}")
        return None

def organize_photos_and_videos(directory):
    """Scan the directory, organize files by date, and move them to respective folders."""
    directory = Path(directory).resolve()

    if not directory.exists() or not directory.is_dir():
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Set up logging inside the target directory
    log_file = setup_logging(directory)
    logging.info(f"Starting photo and video organization in: {directory}")
    print(f"📜 Log file: {log_file}")

    # Get all files (not directories) but EXCLUDE the log file
    files = [f for f in directory.iterdir() if f.is_file() and f != log_file]

    if not files:
        logging.info("No files found in the directory.")
        print("No files found in the directory.")
        return

    for file in files:
        logging.info(f"Processing file: {file.name}")

        # First, try getting the Date Taken from EXIF
        date_taken = get_photo_date_taken(file)

        # If no EXIF date found, fallback to file creation date
        if not date_taken:
            date_taken = get_file_creation_date(file)

        # If no date available, log and skip file
        if not date_taken:
            logging.warning(f"Could not determine date for {file.name}. Skipping.")
            print(f"⚠️ Warning: Could not determine date for {file.name}. Skipping.")
            continue

        # Format date as YYYY-MM-DD
        date_folder_name = date_taken.strftime("%Y-%m-%d")
        date_folder_path = directory / date_folder_name

        # Create date folder if it doesn't exist
        if not date_folder_path.exists():
            date_folder_path.mkdir()
            logging.info(f"Created folder: {date_folder_path}")

        # Move file to the appropriate folder
        new_file_path = date_folder_path / file.name
        shutil.move(str(file), str(new_file_path))
        logging.info(f"Moved {file.name} -> {new_file_path}")
        print(f"✅ Moved {file.name} -> {new_file_path}")

    logging.info("Photo and video organization complete.")
    print("🎉 Organization complete. Check the log file for details.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {SCRIPT_NAME}.py <directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    organize_photos_and_videos(input_directory)
