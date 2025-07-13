def second_largest(nums):
    """
    Return the second largest unique number in the list.
    If it doesn’t exist, return None.
    """
    if not nums:
        return None
    
    # Remove duplicates by converting to set, then back to list
    unique_nums = list(set(nums))
    
    # If less than 2 unique numbers, second largest doesn't exist
    if len(unique_nums) < 2:
        return None
    
    # Sort in descending order and return second element
    unique_nums.sort(reverse=True)
    return unique_nums[1]

# Test cases to verify the function
if __name__ == "__main__":
    
    print(f"second_largest([2,5,1,4,5]) = {second_largest([2,5,1,4,5])}")  # Expected: 4
    
   
    print(f"second_largest([7,7,7]) = {second_largest([7,7,7])}")  # Expected: None
    
    
    print(f"second_largest([10,9,8]) = {second_largest([10,9,8])}")  # Expected: 9