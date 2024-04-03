def reverse_integer(x):
    """
    Reverses the digits of a 32-bit signed integer.

    Args:
    x (int): The integer to be reversed.

    Returns:
    int: The reversed integer, or 0 if it overflows.
    """
    # Handling negative numbers
    sign = -1 if x < 0 else 1
    x *= sign

    # Reversing the integer
    reversed_x = 0
    while x != 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    # Handling overflow
    if reversed_x > 2**31-1 or reversed_x < -2**31:
        return 0

    return reversed_x * sign

# Example usage
try:
    number = 123
    result = reverse_integer(number)
    print("Reversed Integer:", result)
except Exception as e:
    print("Error:", e)
