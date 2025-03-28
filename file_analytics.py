import os
from datetime import datetime

# Extract file metadata (size, creation date, last modified date)
def extract_metadata(file_path):
    if os.path.exists(file_path):
        file_stats = os.stat(file_path)
        metadata = {
            'size': file_stats.st_size,
            'created': datetime.fromtimestamp(file_stats.st_ctime),
            'modified': datetime.fromtimestamp(file_stats.st_mtime)
        }
        print(f"File Metadata for {file_path}: {metadata}")
        return metadata
    print(f"File not found: {file_path}")
    return None
