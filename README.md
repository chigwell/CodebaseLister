[![PyPI version](https://badge.fury.io/py/CodebaseLister.svg)](https://badge.fury.io/py/CodebaseLister)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/codebaselister)](https://pepy.tech/project/codebaselister)

# CodebaseLister

`CodebaseLister` is a Python package designed to document the contents of codebases. It lists all files and their contents, taking into account `.gitignore` rules if required. This tool is useful for developers who need a comprehensive overview of their project's structure and files.

## Installation

To install `CodebaseLister`, you can use pip:

```bash
pip install CodebaseLister
```

## Usage

### As a Python Module

You can use `CodebaseLister` as a module in your Python scripts.

Example:

```python
from codebaselister import CodebaseLister

# Initialize CodebaseLister with optional parameters
lister = CodebaseLister(base_path='path_to_your_project', use_gitignore=True)

# Generate the listing file
listing_details = lister.generate_listing_file()
print(listing_details)
```

### Customizing Your Listing

You can customize the listing by adjusting the initialization parameters of the `CodebaseLister` class, such as `base_path`, `use_gitignore`, and `output_filename`, to fit the specific needs of your project.

## Output Example

When you run `CodebaseLister`, it creates a text file listing all the files in the specified path (excluding those ignored by `.gitignore` if enabled) along with their contents. Here's an example of the output details:

```
{
    "output_filename": "listing_20240113_150223.txt",
    "chars_count": 12345,
    "file_size": 0.5,  # Size in MB
    "files_count": 100
}
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/CodebaseLister/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)
