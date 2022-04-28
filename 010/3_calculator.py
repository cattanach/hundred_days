from art import logo

# operator functions

def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# operations dictionary

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

# operation

def calculator():

    print(logo)

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Choose an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue or 'n' to start a new calculation: ") == "y":
            should_continue = True
            num1 = answer
        else:
            should_continue = False
            calculator()    # calling itself to restart

calculator()
