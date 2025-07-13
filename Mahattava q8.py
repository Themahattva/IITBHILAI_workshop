def is_perfect(n):
    """
    A perfect number equals the sum of its proper divisors
    (excluding itself).
    """
    if n <= 1:
        return False
    
    
    divisor_sum = 0
    
    # Check all numbers from 1 to n-1
    for i in range(1, n):
        if n % i == 0: 
            divisor_sum += i
    
    
    return divisor_sum == n

# Test cases to verify the function
if __name__ == "__main__":
   
    print(f"is_perfect(6) = {is_perfect(6)}")  # Expected: True
    
    
    print(f"is_perfect(28) = {is_perfect(28)}")  # Expected: True
    
    
    print(f"is_perfect(12) = {is_perfect(12)}")  # Expected: False