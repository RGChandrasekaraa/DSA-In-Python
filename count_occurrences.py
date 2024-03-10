def count_occurrences(arr, target):
    """
    Count the number of occurrences of a target number in an array.

    Args:
    - arr (list): The input array.
    - target (int): The number to count occurrences of.

    Returns:
    - int: The number of occurrences of the target number in the array.
    """
    # Initialize a variable to store the count of occurrences
    count = 0
    
    # Iterate through each element in the array
    for num in arr:
        # Check if the current element is equal to the target number
        if num == target:
            # If it is, increment the count
            count += 1
    
    # Return the count of occurrences
    return count

# Get array input from the user
array = list(map(int, input("Enter the array elements separated by space: ").split()))

# Get the target number from the user
target_number = int(input("Enter the target number to count occurrences of: "))

# Call the function and print the result
print("Number of occurrences of", target_number, "in the array:", count_occurrences(array, target_number))
