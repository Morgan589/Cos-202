# ==========================================
#      MATHEMATICAL CALCULATOR (MC)
# ==========================================

while True:
    print("\n=================================")
    print("      MATHEMATICAL CALCULATOR")
    print("=================================")
    print(" +   Addition")
    print(" -   Subtraction")
    print(" *   Multiplication")
    print(" /   Division")
    print(" %   Modulus")
    print(" ^   Power")
    print(" C   Clear")
    print(" OFF Exit")
    print("=================================")

    choice = input("Select an operation: ").upper()

    if choice == "OFF":
        print("Calculator is OFF.")
        break

    elif choice == "C":
        print("\nCalculator Cleared!")
        continue

    elif choice in ["+", "-", "*", "/", "%", "^"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "+":
            print("Answer =", num1 + num2)

        elif choice == "-":
            print("Answer =", num1 - num2)

        elif choice == "*":
            print("Answer =", num1 * num2)

        elif choice == "/":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")

        elif choice == "%":
            if num2 != 0:
                print("Answer =", num1 % num2)
            else:
                print("Error! Division by zero is not allowed.")

        elif choice == "^":
            print("Answer =", num1 ** num2)

    else:
        print("Invalid operation! Please try again.")
