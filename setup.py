"""
setup.py is used to package and distribute a Python project so it can be installed and imported like a standard library or third-party package.

In ML/DL projects, it is commonly used for:

Dependency management: Define required packages (torch, numpy, transformers, etc.).
Package installation: Enable pip install . or pip install -e . (editable/development mode).
Code organization: Make modules importable from anywhere without modifying PYTHONPATH.
Versioning and metadata: Store package name, version, author, license, etc.
Distribution: Build wheels and publish to package repositories.
Custom build steps: Compile C/C++/CUDA extensions when needed.

"""
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This will return list of requirements.
    """
    requirement_lst: List[str] = []
    HYPHEN_E_DOT = "-e ."
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement != HYPHEN_E_DOT:
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt not found!")
    
    # print(requirement_lst)
    return requirement_lst

# print(get_requirements())

setup(
    name="networksecurity",
    version="0.0.1",
    author="Piyush",
    packages=find_packages(),
    install_requires=get_requirements(),
)