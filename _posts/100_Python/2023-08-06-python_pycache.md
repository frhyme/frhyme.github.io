---
title: python - pycache
category:
tags:
---

## Understanding Python's `__pycache__` Folder and Bytecode Optimization

- When you execute Python code on your local computer using the command `python main.py`, you might notice the creation of a `__pycache__` folder within the same directory as the `main.py` script. While this might not directly impact the execution of your code, delving into its mechanics can provide insights into Python's execution process.

- When Python code is executed, the Python compiler translates the human-readable code into bytecode, a lower-level representation that the interpreter can understand and execute efficiently. These bytecode instructions are saved as `.pyc` files, and this is where the `__pycache__` folder comes into play.

- Upon execution, Python checks for the existence of a corresponding `.pyc` file in the `__pycache__` folder. If the file is present and the source code hasn't been modified since the last execution, Python can directly use the bytecode from the `.pyc` file for faster execution, avoiding the need for recompilation.

- However, when you directly run a Python script, such as with the command `python a.py`, no `.pyc` files are generated. The creation of `.pyc` files happens when a script is imported into another script. This mechanism optimizes the execution of frequently used or imported modules, enhancing overall performance.

- In summary, the `__pycache__` folder and `.pyc` files are integral to Python's effort in achieving a balance between development convenience and runtime efficiency. While they might seem like minor artifacts, they play a significant role in enhancing the execution speed of Python code, especially in larger projects or when using imported modules.

### Six roles of `__pycache__`

- and there are six roles that `__pycache__` do:

1. **Bytecode Storage**: When you run a Python script (`.py` file), the Python interpreter compiles the source code into bytecode, which is a lower-level representation of the code that the interpreter can execute. Instead of recompiling the source code every time you run the script, the interpreter stores the compiled bytecode in `.pyc` files.
- If you want to interpret the python file to python byte code, run below code on your command. Then you will see that the folder named `__pycache__` is generated and python byte code file was created in that folder.

```sh
python -m module_name main.py
```

1. **Caching for Performance**: The `__pycache__` directory acts as a cache for these compiled bytecode files. Caching the compiled bytecode provides a significant performance boost when you run the same script multiple times. The interpreter can reuse the precompiled bytecode, reducing the need for repetitive parsing and compilation of the source code.

1. **Version Compatibility**: The filenames of the `.pyc` files include a version number to ensure compatibility across different Python interpreter versions. This allows multiple versions of Python to coexist on the same system without conflicts.

1. **Platform Independence**: The `__pycache__` directory helps ensure platform independence for the cached bytecode. Bytecode stored in the `__pycache__` directory is not specific to the underlying hardware or operating system, making it portable across different systems.

1. **Updating Cached Files**: The Python interpreter checks the timestamps of the `.py` files and corresponding `.pyc` files. If a `.pyc` file doesn't exist or is older than its corresponding `.py` file, the interpreter recompiles the source code and updates the `.pyc` file.

1. **Cleanup**: The `__pycache__` directory doesn't contain user-editable files. It is automatically managed by the Python interpreter, which creates, updates, and deletes `.pyc` files as needed. It is safe to let the interpreter handle the contents of this directory.

### Read python byte code

- if you want to read python byte code, use below code. Python byte code doesn't provided readable code like python source code, but it gives you a deeper insight about how python compiler works on running python source code.

```python
import dis
from pathlib import Path


def read_pyc_file(file_path: str):
    path = Path(file_path)
    with path.open('rb') as f:
        magic = f.read(4)
        timestamp = f.read(4)
        code_object = f.read()
    print(f'magic: {magic}')
    print(f'timestamp: {timestamp}')
    print('== code object')
    dis.dis(code_object)
    print('-----------------')


if __name__ == '__main__':
    print("= This is main function")
    read_pyc_file('./__pycache__/pycache_test.cpython-37.pyc')
    print('= main function done')
```

### Read timestamp

- A timestamp is utilized to verify whether the Python bytecode corresponds to the most recent compiled version of the current Python source code. When alterations are made to the Python source, any existing bytecode becomes obsolete. If the compiler remains unaware that the old Python bytecode no longer aligns with the current source code and proceeds to execute outdated bytecode instead of the updated source code, erroneous outcomes can arise.

- When encountering an import statement for a module, the Python interpreter follows a sequence of steps to determine whether regeneration of the corresponding `.pyc` file is necessary, which hinges on timestamp comparisons.

1. **Locating the `.pyc` File**:
- The interpreter searches for a `.pyc` file within the `__pycache__` directory or the same directory as the source file. The filename of the `.pyc` file incorporates the module name along with the Python version number.

1. **Timestamp Comparison**:
 - Upon finding a `.pyc` file, the interpreter retrieves the timestamp stored in the header of the file. This timestamp reflects when the `.pyc` file was originally generated.
 - The following code snippet seemingly extracts the timestamp stored within the `.pyc` file. Nevertheless, despite my attempts to modify the source code and recompile it, the timestamp remains unaltered; it consistently remains fixed at zero. It's plausible that my approach was flawed. Should anyone possess a solution for ascertaining the timestamp of Python bytecode, kindly share your insights. I've realized that this timestamp might not necessarily signify direct modifications to the source code.

```python
import struct
from pathlib import Path

def read_pyc_timestamp(pyc_file_path):
    path = Path(pyc_file_path)
    with path.open('rb') as f:
        magic_and_timestamp = f.read(8)
    # Unpack the timestamp from the binary data
    timestamp = struct.unpack('<I', magic_and_timestamp[4:8])[0]
    return timestamp


if __name__ == '__main__':
    pyc_file_path = './__pycache__/pycache_test.cpython-37.pyc'
    timestamp = read_pyc_timestamp(pyc_file_path)
    print(f'Timestamp: {timestamp}')
```

## Reference

- [stackoverflow - how does the python interpreter know when to compile and update a pyc file](https://stackoverflow.com/questions/23775760/how-does-the-python-interpreter-know-when-to-compile-and-update-a-pyc-file)
