# Unclosed File Bug in Python

This repository demonstrates a common error in Python: forgetting to close files properly.  The `bug.py` file shows code that might fail to close a file if an exception occurs.  The solution, in `bugSolution.py`, uses a `try...except...finally` block to ensure the file is always closed.