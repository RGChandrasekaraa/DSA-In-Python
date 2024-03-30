def find_number_position(arr, target):

    if not isinstance(arr, list):
        raise TypeError("The 'arr' argument must be a list of integers.")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in 'arr' must be integers.")
    if not isinstance(target, int):
        raise TypeError("The 'target' argument must be an integer.")
    if len(arr) == 0:
        raise ValueError("The 'arr' list cannot be empty.")

    # Attempt to find the index of the target number
    try:
        return arr.index(target)
    except ValueError:
        # If target is not in the list
        return "Target not present in the array."

# Example usage
try:
    arr = [3, 5, 1, 2, 9]
    target = 2
    result = find_number_position(arr, target)
    print(f"Position of {target} in the array: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
