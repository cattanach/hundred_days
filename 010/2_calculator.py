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

# first operation

num1 = int(input("What's the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Choose an operator from the list above: ")
num2 = int(input("What's the second number? "))

first_answer = operations[operation_symbol](num1, num2)

# OR

# calculation_function = operations[operation_symbol]                 
# first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# second operation

operation_symbol = input("Choose another operator: ")
num3 = int(input("What's the third number? "))

second_answer = operations[operation_symbol](first_answer, num3) 

# OR

# second_answer = operations[operation_symbol](operations[operation_symbol](num1, num2), num3) 

# OR

# calculation_function = operations[operation_symbol]                          
# second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")