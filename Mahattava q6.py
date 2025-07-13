def fibonacci(n):
    """
    Return the n-th Fibonacci number (F1=1, F2=1).
    Use iteration, not recursion.
    """
    if n == 1 or n == 2:
        return 1
    
    # Initialize first two Fibonacci numbers
    a, b = 1, 1  
    
    # Iterate from 3 to n to calculate subsequent Fibonacci numbers
    for i in range(3, n + 1):
        a, b = b, a + b  
    
    return b

# Test cases to verify the function
if __name__ == "__main__":
    
    print(f"fibonacci(1) = {fibonacci(1)}")  # Expected: 1
    
    
    print(f"fibonacci(7) = {fibonacci(7)}")  # Expected: 13
    
    
    print(f"fibonacci(10) = {fibonacci(10)}")  # Expected: 55