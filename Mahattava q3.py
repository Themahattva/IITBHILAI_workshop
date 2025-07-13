def trailing_zeros(n):
    """
    Return the number of trailing zeros in n! by counting
    how many times 5 divides factors up to n.
    """
    if n < 5:
        return 0
    
    count = 0
    power_of_5 = 5
    
    # Count multiples of 5, 25, 125, etc.
    while power_of_5 <= n:
        count += n // power_of_5  # Add count of multiples of current power of 5
        power_of_5 *= 5  # Move to next power of 5
    
    return count

# Test cases to verify the function
if __name__ == "__main__":
   
    print(f"trailing_zeros(5) = {trailing_zeros(5)}")  # Expected: 1
    
    
    print(f"trailing_zeros(100) = {trailing_zeros(100)}")  # Expected: 24
    
    
    print(f"trailing_zeros(3) = {trailing_zeros(3)}")  # Expected: 0