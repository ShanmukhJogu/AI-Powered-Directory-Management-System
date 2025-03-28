from transformers import pipeline

# Load zero-shot classification model for categorization
classifier = pipeline('zero-shot-classification')

# Categorize a file based on its content (text files)
def categorize_file(file_content):
    categories = ['invoice', 'contract', 'report', 'memo', 'email']
    result = classifier(file_content, candidate_labels=categories)
    category = result['labels'][0]  # Get top category
    print(f"File categorized as: {category}")
    return category

# Example function to read file content
def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content
