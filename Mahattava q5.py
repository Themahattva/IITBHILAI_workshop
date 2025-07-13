def count_letters(text):
    """
    Return a tuple (vowels, consonants) in the text.
    Count only English letters, ignore case.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
   
    for char in text:
        if char.isalpha():  # Check if character is a letter
            if char in vowels:  # Check if it's a vowel
                vowel_count += 1
            else:  # It's a consonant
                consonant_count += 1
    
    return (vowel_count, consonant_count)

# Test cases to verify the function
if __name__ == "__main__":
   
    print(f'count_letters("Data Science") = {count_letters("Data Science")}')  # Expected: (5, 5)
    
    
    print(f'count_letters("IIT Bhilai") = {count_letters("IIT Bhilai")}')  # Expected: (4, 4)
    
    
    print(f'count_letters("1234!") = {count_letters("1234!")}')  # Expected: (0, 0)