# codebaselister/main.py
import os
import pathspec
from datetime import datetime

class CodebaseLister:
    def __init__(self, base_path=os.getcwd(), use_gitignore=True, output_filename=None):
        self.base_path = base_path
        self.use_gitignore = use_gitignore
        self.output_filename = output_filename or f"listing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    def load_gitignore(self):
        try:
            with open(os.path.join(self.base_path, '.gitignore'), 'r') as file:
                return pathspec.PathSpec.from_lines('gitwildmatch', file)
        except FileNotFoundError:
            return None

    def list_files(self):
        if self.use_gitignore:
            spec = self.load_gitignore()
        else:
            spec = None

        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                file_path = os.path.join(root, file)
                if spec and spec.match_file(file_path):
                    continue
                yield file_path

    def read_file_content(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {e}"

    def generate_listing_file(self):
        file_paths = self.list_files()
        chars_count = 0
        with open(self.output_filename, 'w') as outfile:
            for path in file_paths:
                if path == self.output_filename:
                    continue
                outfile.write(f"# {path}:\n")
                content = self.read_file_content(path)
                outfile.write(content + "\n\n")
                chars_count += len(content)
        # file_size in MB
        file_size = os.path.getsize(self.output_filename) / 1024 / 1024
        return {
            "output_filename": self.output_filename,
            "chars_count": chars_count,
            "file_size": file_size,
            "files_count": len(list(self.list_files()))
        }

"""def main():
    lister = CodebaseLister()
    lister.generate_listing_file()

if __name__ == "__main__":
    main()"""
