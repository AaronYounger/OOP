while(True):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    option = input("Enter your choice: ")
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    if option == "1":
        Add = n1 + n2
        print("The sum is: ", Add)
    elif option == "2":
        sub = n1 - n2
        print("The difference is: ", sub)
    elif option == "3":
        Multiply = n1 * n2
        print("The product is: ", Multiply)
    elif option == "4":
        if n2 == 0:
            print("Number is invalid, Choose New Number For Denominator")
        Division = n1 / n2
        print("The quotient is: ", Division)
    elif option == "5":
        break
print("Your the best")

