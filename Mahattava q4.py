import re

def is_palindrome(s):
    """
    Return True if string s reads the same forwards and backwards.
    Ignore case and non-alphanumeric characters.

    """
    cleaned = ""
    for char in s:
        if char.isalnum():  # Check if character is alphanumeric
            cleaned += char.lower()  
    
    
    return cleaned == cleaned[::-1]

# Test cases to verify the function
if __name__ == "__main__":
    
    print(f'is_palindrome("Madam") = {is_palindrome("Madam")}') 
    
    
    print(f'is_palindrome("Step on no pets") = {is_palindrome("Step on no pets")}') 
    
    print(f'is_palindrome("Hello, World!") = {is_palindrome("Hello, World!")}')  # 