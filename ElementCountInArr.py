def count_elements(arr):
    """
    Counts the occurrences of each element in the given array.

    :param arr: List of elements (numbers, strings, etc.)
    :return: Dictionary with elements as keys and their counts as values
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    element_count = {}

    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    return element_count

# Example usage
array = [1, 2, 3, 2, 4, 1, 2, 3, 4, 4]
print(count_elements(array))
