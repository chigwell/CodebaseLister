# setup.py
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CodebaseLister',
    version='0.0.1',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='A package to list and document the contents of codebases, optionally using .gitignore rules.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/CodebaseLister',
    packages=find_packages(),
    install_requires=[
        'pathspec',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires='>=3.6',
)
