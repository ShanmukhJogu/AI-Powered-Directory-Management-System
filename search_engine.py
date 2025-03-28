from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os 

class FileSearch:
    def __init__(self, file_contents, file_paths):
        self.vectorizer = TfidfVectorizer()
        self.file_contents = file_contents
        self.file_paths = file_paths
        self.tfidf_matrix = self.vectorizer.fit_transform(file_contents)

    # Search for files based on a query
    def search(self, query):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)
        return [self.file_paths[i] for i in similarities.argsort()[0][-5:]]  # Return top 5 matches

    # Example function to load file contents
    def load_file_contents(self, directory):
        file_paths = []
        file_contents = []
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_paths.append(file_path)
                with open(file_path, 'r') as f:
                    file_contents.append(f.read())
        return file_contents, file_paths
