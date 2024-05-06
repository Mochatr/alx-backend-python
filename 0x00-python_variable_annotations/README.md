# Python - Variable annotations

![Variable Annotations] (https://i.redd.it/y9y25tefi5401.png)

## Concepts

This project is designed around the "Advanced Python" concept with a focus on type annotations, duck typing, and code validation using mypy.

## Ressources

For this project, i utilized the following ressources:
- [Python 3 typing documentation] (https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet] (https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Learning Objectives

This project was made in order for you to explain the following topics without the need to refer to external resources:

- **Type Annotations in Python 3**: Understanding how to use type annotations to explicitly specify the types of variables, function parameters, and return types.
- **Function Signatures and Variable Types**: How to use type annotations to define function signatures and declare variable types, enhancing code readability and maintainability.
- **Duck Typing**: The concept of duck typing in Python, and how it allows for more flexible and adaptable code.
- **Code Validation with mypy**: Using mypy to statically analyze and validate Python code for type consistency and correctness.

## Requirements

### General

- **Editors**: Code should be written in vi, vim, or emacs.
- **Environment**: All scripts must run on Ubuntu 18.04 LTS using Python 3.7.
- **Script Execution**: The first line of all your scripts should be `#!/usr/bin/env python3` to ensure they are executable in a Unix-like environment.
- **Code Style**: Adherence to the Pycodestyle (version 2.5) is required for all Python files.
- **Documentation**:
  - Modules: Every module must have documentation accessible via `python3 -c 'print(__import__("my_module").__doc__)'`.
  - Classes: Each class should have its own documentation, retrievable with `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`.
  - Functions: Document every function inside and outside of classes. Documentation can be verified with `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`.
- **Executable Files**: All Python files must be executable. Ensure this by modifying the file permissions accordingly.
- **New Line Requirement**: Every file should end with a newline.

## Additional Information

All documentation should consist of full sentences explaining the purpose and functionality of the module, class, or method. The documentation's quality and length will be scrutinized to ensure clarity and completeness.
