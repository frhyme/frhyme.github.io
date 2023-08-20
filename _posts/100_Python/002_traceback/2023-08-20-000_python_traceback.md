---
title: python - traceback
category: python
tags: python traceback
---

## python - traceback

- When dealing with exceptions in Python, we would make use of the traceback module, as demonstrated in the code snippet below.
- In cases where errors occur during the execution of Python code, the traceback module traces back from the most recent function call to the root call in its call stack. This enables us to identify the specific line and function that triggered the error.

```python
import traceback


def f1():
    return f2()


def f2():
    return f3()


def f3():
    return 1 / 0


if __name__ == '__main__':
    try:
        f1()
    except ZeroDivisionError:
        print("== Zero Division Error")
        traceback.print_exc()

        exception_log = traceback.format_exc()
        print(exception_log)
```

- traceback

```log
== Zero Division Error
Traceback (most recent call last):
  File "exception_test.py", line 18, in <module>
    f1()
  File "exception_test.py", line 5, in f1
    return f2()
  File "exception_test.py", line 9, in f2
    return f3()
  File "exception_test.py", line 13, in f3
    return 1 / 0
ZeroDivisionError: division by zero
Traceback (most recent call last):
  File "exception_test.py", line 18, in <module>
    f1()
  File "exception_test.py", line 5, in f1
    return f2()
  File "exception_test.py", line 9, in f2
    return f3()
  File "exception_test.py", line 13, in f3
    return 1 / 0
ZeroDivisionError: division by zero
```

## how python interpreter run the python code

- Just as you use the `traceback` module to manage exceptions, the Python interpreter also employs the same module to handle exceptions and display error log messages.
- When you run the command `python main.py` to execute a Python script named `main.py`, several steps take place behind the scenes:

1. **Interpreter Invocation:**
  - The command `python` is the Python interpreter. When you run it, it's invoked to execute the specified Python script.

1. **Parsing and Compilation:**
  - The Python interpreter reads the contents of the `main.py` file, parses the code, and compiles it into bytecode. The bytecode is an intermediate representation of the code that the interpreter can execute.

1. **Execution:**
  - The interpreter starts executing the bytecode line by line. It follows the control flow of the script, executing each statement and expression.

1. **Exception Handling:**
  - If an unhandled exception occurs during execution (e.g., division by zero, name error, etc.), the interpreter generates an exception object. The exception object contains information about the type of exception and additional details.

1. **Traceback Generation:**
  - The interpreter generates a traceback using the `traceback` module. This traceback includes information about the sequence of function calls that led to the exception. The traceback contains file names, line numbers, and function names.

1. **Traceback Display:**
  - The interpreter displays the traceback along with the error message to the console. This provides information about where the exception occurred and the context in which it was raised.

1. **Program Termination:**
  - Once the script execution is complete or when an unhandled exception occurs, the script terminates. Any resources that were opened during execution are typically closed.
