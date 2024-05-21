#FizzBuzz

def fizz_buzz(number):
    """
    Generate FizzBuzz sequence up to the given number.

    Args:
    - number (int): The upper limit of the sequence.

    Returns:
    - list of str: FizzBuzz sequence up to the given number.
    """
    fizz_buzz_sequence = []
    try:
        if number <= 0:
            raise ValueError("Number must be greater than zero.")
        
        for i in range(1, number + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            fizz_buzz_sequence.append(output or str(i))  # If output is empty, add the number itself
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
    
    return fizz_buzz_sequence

def main():
    try:
        number = int(input("Enter Number: "))
        fizz_buzz_result = fizz_buzz(number)
        if fizz_buzz_result:
            print("\n".join(fizz_buzz_result))
    except ValueError as ve:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
