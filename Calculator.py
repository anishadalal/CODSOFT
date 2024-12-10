def calculator():
    print("Simple Calculator")
    print("Select an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
            else:
                print("Division by zero is not possible!")
    except ValueError:
        print("Invalid input!")

calculator()
