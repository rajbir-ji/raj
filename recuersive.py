from functools import lru_cache

@lru_cache(maxsize=None) # Caches results of the function calls
def fibonacci_recursive_memoized(n):
    """
    Calculates the 'n'-th Fibonacci number recursively with memoization.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_memoized(n - 1) + fibonacci_recursive_memoized(n - 2)

# Example usage (to get a specific Fibonacci number):
term_index = 9
fib_number = fibonacci_recursive_memoized(term_index)
print(f"The {term_index}-th Fibonacci number is: {fib_number}")