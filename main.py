import os
from pathlib import Path

DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')
IGNORED_EXTENSIONS = [".DS_Store", ".localized"]
DIRECTORY_MAP = {
    "Documents": [".pdf", ".rtf", ".txt", ".doc"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Disc": [".bin", ".dmg", ".iso", ".toast", ".vcd"],
    "Data": [".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml", ".json"],
}


def organize_downloads():
    files = get_files_in_dir(DOWNLOADS_DIR)

    print(f"Found {len(files)} file(s).")

    if len(files) == 0:
        return

    move_files_to_dirs(files)


def get_files_in_dir(directory):
    files = []

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and file not in IGNORED_EXTENSIONS:
            files.append(file)

    return files


def move_files_to_dirs(files):
    file_counter = 0

    for file in files:
        directory = pick_directory(file)

        if directory == "Other":
            continue

        directory_path = os.path.join(DOWNLOADS_DIR, directory)

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_path = os.path.join(DOWNLOADS_DIR, file)
        os.rename(file_path, os.path.join(directory_path, file))

        file_counter += 1

    if file_counter == 0:
        print("No files were moved.")
    else:
        print(f"Moved {file_counter} file(s).")


def pick_directory(file):
    for directory, extensions in DIRECTORY_MAP.items():
        if Path(file).suffix in extensions:
            return directory

    print(f"Couldn't find a directory for {file}")

    return "Other"


if __name__ == '__main__':
    organize_downloads()
