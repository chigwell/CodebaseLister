# codebaselister/main.py
import os
import pathspec
from datetime import datetime
class CodebaseLister:
    """A class to list and document the contents of codebases, optionally using .gitignore rules."""

    def __init__(self, base_path=os.getcwd(), use_gitignore=True, output_filename=None):
        """
        Initialize the CodebaseLister object.

        :param base_path: The base path of the codebase to list. Defaults to the current working directory.
        :type base_path: str
        :param use_gitignore: Whether to use .gitignore rules when listing files. Defaults to True.
        :type use_gitignore: bool
        :param output_filename: The name of the output listing file. Defaults to a timestamped file name.
        :type output_filename: str or None
        """
        self.base_path = base_path
        self.use_gitignore = use_gitignore
        self.output_filename = output_filename or f"listing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    def load_gitignore(self):
        """
        Load .gitignore rules from the codebase's base path.

        :return: A PathSpec object representing the .gitignore rules, or None if no .gitignore file is found.
        :rtype: pathspec.PathSpec or None
        """
        try:
            with open(os.path.join(self.base_path, '.gitignore'), 'r') as file:
                return pathspec.PathSpec.from_lines('gitwildmatch', file)
        except FileNotFoundError:
            return None

    def list_files(self):
        """
        Generator function to yield file paths within the codebase that match the specified rules.

        :yield: The file path as a string.
        :rtype: str
        """
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
        """
        Read the content of a file as a string.

        :param file_path: The path of the file to read.
        :type file_path: str
        :return: The content of the file as a string, or an error message if the file cannot be read.
        :rtype: str
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {e}"

    def generate_listing_file(self):
        """
        Generate a listing file containing the contents of all files in the codebase that match the specified rules.

        :return: A dictionary containing metadata about the generated listing file, including the output file name,
                 character count, file size in MB, and number of files listed.
        :rtype: dict
        def _read_files_content(self, file_paths):
        chars_count = 0
        contents = []
        for path in file_paths:
            if path == self.output_filename:
                continue
            content = self.read_file_content(path)
            chars_count += len(content)
            contents.append(content)
        return chars_count, contents

    def generate_listing_file(self):
        file_paths = self.list_files()
        chars_count, contents = self._read_files_content(file_paths)
        with open(self.output_filename, 'w') as outfile:
            for idx, path in enumerate(file_paths):
                if path == self.output_filename:
                    continue
                outfile.write(f"# {path}:\n")
                outfile.write(contents[idx] + "\n\n")
        # file_size in MB
        file_size = os.path.getsize(self.output_filename) / 1024 / 1024
        return {
            "output_filename": self.output_filename,
            "chars_count": chars_count,
            "file_size": file_size,
            "files_count": len(file_paths)
        }

"""def main():
    lister = CodebaseLister()
    lister.generate_listing_file()

if __name__ == "__main__":
    main()"""
