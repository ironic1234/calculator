import math

history = []

while True:
    command = input("Command: ")
    while not (command == "history" or command == "calculator"):
        command = input("Command: ")
    
    if (command == "calculator"):
        while True:
            firstnumber = input("What is the first number: ")
            if firstnumber == "exit":
                break
            operator = input("What is the operator: ")
            if operator == "exit":
                break
            if not (operator == "!" or operator == "sqrt" or operator == "ceil" or operator == "floor"):
                secondnumber = input("What is your second number: ")
                if secondnumber == "exit":
                    break

            if operator == "+":
                equation = (firstnumber + " + " + secondnumber + " = " + str(float(firstnumber) + float(secondnumber)))
                history.append(equation)
                print(equation) 

            elif operator == "-":
                equation = (firstnumber + " - " + secondnumber + " = " + str(float(firstnumber) - float(secondnumber)))
                history.append(equation)
                print(equation)   

            elif operator == "*":
                equation = (firstnumber + " * " + secondnumber + " = " + str(float(firstnumber) * float(secondnumber)))
                history.append(equation)
                print(equation)

            elif operator == "/":
                equation = (firstnumber + " / " + secondnumber + " = " + str(float(firstnumber) / float(secondnumber)))
                history.append(equation)
                print(equation)

            elif operator == "%":
                equation = (firstnumber + " % " + secondnumber + " = " + str(float(firstnumber) % float(secondnumber)))
                history.append(equation)
                print(equation)

            elif operator == "**":
                equation = (firstnumber + " ** " + secondnumber + " = " + str(float(firstnumber) ** float(secondnumber)))
                history.append(equation)
                print(equation)

            elif operator == "!":
                equation = (firstnumber + "! = " + str(math.factorial(int(firstnumber))))
                history.append(equation)
                print(equation)

            elif operator == "sqrt":
                equation = ("√" + firstnumber + " = " + str(math.sqrt(float(firstnumber))))
                history.append(equation)
                print(equation)

    elif (command == "history"):
        for i in history:
            print(i)