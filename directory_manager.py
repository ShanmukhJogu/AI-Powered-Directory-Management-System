import os
import shutil

# Create a directory
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created at {path}")
        return True
    print(f"Directory already exists at {path}")
    return False

# Move a file
def move_file(src, dest):
    if os.path.exists(src):
        shutil.move(src, dest)
        print(f"File moved from {src} to {dest}")
        return True
    print(f"Source file not found: {src}")
    return False

# List all files in a directory
def list_files(directory):
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return []

# Delete a file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File deleted: {file_path}")
        return True
    print(f"File not found: {file_path}")
    return False
