def rotate_array(nums, k):
    """
    Rotate the array `nums` to the right by `k` steps.
    
    Args:
    nums (List[int]): The input array.
    k (int): The number of steps to rotate the array.

    Returns:
    List[int]: The array after rotation.
    """
    # Ensure the rotation step is not greater than the length of the array
    k = k % len(nums)

    # Define a function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    # Reverse the entire array
    reverse(0, len(nums) - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the rest of the array
    reverse(k, len(nums) - 1)

    return nums

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))