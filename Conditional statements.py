## Conditional Statements
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
elif c > a and c > b:
    print("C is greater")
else:
    print("They are equal")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Enter operator value; +, -, *, /")

if operator == "+":
    print("The sum is:", number1 + number2)
elif operator == "-":
    print("The difference is:", number1 - number2)
elif operator == "*":
    print("The product is:", number1 * number2)
elif operator == "/":
    print("The quotient is:", number1 / number2)
else:
    print("Not a valid operator")

## Grading code

course1 = int(input("Enter the grade for course1: "))
course2 = int(input("Enter the grade for course2: "))
course3 = int(input("Enter the grade for course3: "))
course4 = int(input("Enter the grade for course4: "))
course5 = int(input("Enter the grade for course5: "))

total = course1 + course2 + course3 + course4 + course5
print("Your total points is:", total)

total_percentage = ((total/500)*100)
print(total_percentage)

if total_percentage <100 and total_percentage >=90:
    print("Grade A:", total_percentage)
elif total_percentage <90 and total_percentage >=80:
    print("Grade B:", total_percentage)
elif total_percentage <80 and total_percentage >=70:
    print("Grade C:", total_percentage)
elif total_percentage <70 and total_percentage >=60:
    print("Grade D:", total_percentage)
elif total_percentage <60 and total_percentage >=0:
    print("Grade F:", total_percentage)