def is_armstrong(n):
    """
    An Armstrong number is an n-digit number that equals
    the sum of each digit raised to the power n.
    e.g. 153 = 1^3 + 5^3 + 3^3
    """
    s = str(n)
    num_digits = len(s)  
    total = 0
    
    
    for digit_char in s:
        digit = int(digit_char) 
        total += digit ** num_digits  
    
    
    return total == n

# Test cases to verify the function
if __name__ == "__main__":
   
    print(f"is_armstrong(153) = {is_armstrong(153)}")  # Expected: True
    
    print(f"is_armstrong(370) = {is_armstrong(370)}")  # Expected: True
    
    print(f"is_armstrong(123) = {is_armstrong(123)}")  # Expected: False
