import time
import os
from ai_categorization import categorize_file, read_file
# Monitor directory for new files
def monitor_directory(directory, interval=5):
    print(f"Monitoring {directory} for changes...")
    while True:
        files = os.listdir(directory)
        print(f"Current files: {files}")
        time.sleep(interval)  # Sleep for the specified interval (in seconds)

# Automate actions on new files (e.g., auto-categorize)
def automate_actions(directory):
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_content = read_file(file_path)
            category = categorize_file(file_content)
            print(f"Automated categorization: {file} -> {category}")
