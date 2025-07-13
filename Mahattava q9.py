import re

def is_isogram(s):
    """
    Return True if the string has no repeating letters.
    Ignore case and non-letters.
    """
    cleaned = ""
    for char in s:
        if char.isalpha():  
            cleaned += char.lower()  
    
    # Use set to detect duplicates
    # If length of set equals length of string, no duplicates exist
    return len(set(cleaned)) == len(cleaned)

# Test cases to verify the function
if __name__ == "__main__":
    
    print(f'is_isogram("Machine") = {is_isogram("Machine")}')  # Expected: False
    
    print(f'is_isogram("Algorithm") = {is_isogram("Algorithm")}')  # Expected: True
    
    print(f'is_isogram("Dermatoglyphics") = {is_isogram("Dermatoglyphics")}')  # Expected: True