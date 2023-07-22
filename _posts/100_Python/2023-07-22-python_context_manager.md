---
title: python - context manager
category: python
tags: python context
---

## python - context manager

- A context manager in Python is a programming construct that allows you to manage the setup and teardown of resources in a structured and convenient way. It's primarily used to ensure that certain operations are performed before and after a block of code is executed. The primary purpose of context managers is to handle resource allocation and deallocation in a clean and safe manner.
- Context managers are implemented using two special methods in Python classes: `__enter__()` and `__exit__()`. These methods define what happens when a context is entered (before the indented block of code) and when it is exited (after the indented block of code).

- Here's how the context manager works in detail:
1. Entering the Context (`__enter__()` method):
- When a context is entered (at the beginning of the with statement), the `__enter__`() method of the context manager is invoked. This method is responsible for setting up the necessary resources or performing any other actions required before executing the indented block of code.
2. Executing the Indented Block:
- Once the `__enter__`() method completes its execution, the indented block of code under the with statement is executed. This is where you perform the main operations that require the managed resource.
3. Exiting the Context (`__exit__()` method):
- After the indented block of code is executed (whether normally or due to an exception), the `__exit__()` method of the context manager is called. This method handles resource cleanup and any necessary finalization steps. If an exception occurs within the indented block, the __exit__() method is still called to ensure that resources are properly released or cleaned up.

The `__exit__`() method can accept three arguments: `exc_type`, `exc_value`, and `traceback`. These arguments provide information about any exception that occurred within the indented block. If the `__exit__()` method returns False or raises an exception, the exception will be propagated to the caller; otherwise, it will be suppressed.

Python provides two common ways to implement context managers:

- Using the contextlib module:
  - The contextlib module provides a decorator called contextmanager, which allows you to create a context manager using a generator function. This is a simpler way to create lightweight context managers for simple cases.

- Implementing a class with `__enter__()` and `__exit__()` methods:
  - You can create a custom context manager by implementing a class with the `__enter__()` and `__exit__()` methods. This gives you more flexibility and control over the context management process, making it suitable for complex scenarios.

- Here's an example of a custom context manager using the contextlib module:

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Setup code (before entering the context)
    print("Entering the context")
    yield   # This is where the indented block will be executed
    # Cleanup code (after exiting the context)
    print("Exiting the context")

# Using the context manager with the 'with' statement
with my_context_manager():
    print("Inside the context")
```

- Here's an example of a custom context manager using the class methods

```python
class MyContextManager:
    def __enter__(self):
        # Setup code (before entering the context)
        print("Entering the context")
        # You can return an object if needed, which will be assigned to the variable after 'as'
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup code (after exiting the context)
        print("Exiting the context")
        # If an exception occurred, handle it here or return False to propagate it to the caller.
        # If you return True, the exception will be suppressed.
        return False


# Using the context manager with the 'with' statement
with MyContextManager() as cm:
    print("Inside the context")
```
