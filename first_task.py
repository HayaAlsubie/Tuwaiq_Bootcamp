print('Hi I am Haya and this my first task in Data Science and AI with Tuwaiq Academy')

def add_two_numbers():
    """
    Function to add two numbers taken from user input
    """
    try:
        # Get first number from user
        num1 = float(input("Enter the first number: "))

        # Get second number from user
        num2 = float(input("Enter the second number: "))

        # Calculate the sum
        result = num1 + num2

        # Display the result
        print(f"The sum of {num1} and {num2} is: {result}")

        return result

    except ValueError:
        print("Error: Please enter valid numbers only!")
        return None

# Call the function to execute
add_two_numbers()
