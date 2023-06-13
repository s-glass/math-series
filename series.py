"""
# Create a fibonacci function with docstring and param (n) that returns nth value in fibonacci series using recursion or iteration.

# Create a lucas function with docstring returning the nth value in the lucas series using recursion or iteration.

# Create a function called sum_series with one required parameter and two optional parameters. The required will determine which element to print. The optionals will have default values of 0 and 1 and will determine the first two values for the series to be produced.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)