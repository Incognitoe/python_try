def calculate_square(number):
    return number ** 2

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    result = calculate_square(user_input)
    print(f"The square of {user_input} is {result}")