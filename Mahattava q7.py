def swap(a, b):
    """
    Swap two integers without using a third variable.
    Return the new pair (a, b).
    """
    a, b = b, a
    return a, b

if __name__ == "__main__":
    
    print(f"swap(3, 5) = {swap(3, 5)}")  # Expected: (5, 3)
    
    
    print(f"swap(-1, 10) = {swap(-1, 10)}")  # Expected: (10, -1)
    
    
    print(f"swap(0, 0) = {swap(0, 0)}")  # Expected: (0, 0)