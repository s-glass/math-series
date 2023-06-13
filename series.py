"""
# Create a fibonacci function with docstring and param (n) that returns nth value in fibonacci series using recursion or iteration.

# Create a lucas function with docstring returning the nth value in the lucas series using recursion or iteration.

# Create a function called sum_series with one required parameter and two optional parameters. The required will determine which element to print. The optionals will have default values of 0 and 1 and will determine the first two values for the series to be produced.

# Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, parameter1, parameter2):
    if parameter1 == 0 and parameter2 == 1:
        return fibonacci(n)
    elif parameter1 == 2 and parameter2 == 1:
        return lucas(n)
    else:
        return sum_series(n-1) + sum_series(n-2)