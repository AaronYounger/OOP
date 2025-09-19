myEmployees = {}

while True:
    print("1. Add an Employee")
    print("2. Remove an Employee")
    print("3. Update an Existing Employee's information")
    print("4. Display Employee Information's")
    print("5. Exit Application")
    options = input("Enter Number: ")

    if options == "1":
        emid = int(input("Enter Employee ID: "))
        Emname = input("Enter Employee Name: ")
        Bp = int(input("Enter Employee's BasicPay: "))
        allowance = int(input("Enter Employees allowance: "))
        Deductions = (int(input("Enter Employees reduction: ")))
        Taxes = (int(input("Enter Employees Taxes: ")))
        NetPay = Bp + allowance
        GrossPay = NetPay - (Deductions + Taxes)

        myEmployees.update({
            emid:{
            "Employee Name" : Emname,
            "Basic Pay" : Bp,
            "Employee Allowance" : allowance,
            "Employee Deductions" : Deductions,
            "Employee Taxes" : Taxes,
            "Employee Net Pay" : NetPay,
            "Employee Gross Pay" : GrossPay

        }
        })
    elif options == "2":
        emid = int(input("Enter Employee ID: "))
        if emid in myEmployees:
            del myEmployees[emid]
        else:
            print("Employee ID not Found")
            continue
    elif options == "3":
        emid = int(input("Enter Employee ID: "))
        if emid in myEmployees:
            Emname = input("Enter Employee Name: ")
            Bp = int(input("Enter Employee's BasicPay Allowance: "))
            allowance = int(input("Enter Employees allowance: "))
            Deductions = (int(input("Enter Employees reduction: ")))
            Taxes = (int(input("Enter Employees Taxes: ")))
            NetPay = Bp + allowance
            GrossPay = NetPay - (Deductions + Taxes)
            myEmployees[emid] = {
                "Employee Name" : Emname,
                "Basic Pay" : Bp,
                "Employee Allowance" : allowance,
                "Employee Deductions" : Deductions,
                "Employee Taxes" : Taxes,
                "Employee Net Pay" : NetPay,
                "Employee Gross Pay" : GrossPay
            }
        else:
                print("Employee ID Not Found")
                continue
    elif options == "4":
        if len(myEmployees) > 0:
            print(myEmployees)
        else:
            print("The List is Empty")
    elif options == "5":
            break






