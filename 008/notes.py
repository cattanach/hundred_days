def function_1():
    print("  This  ")
    print(" is  a ")
    print("function")

function_1()

def greet(name):
    print(f"hey {name}")

greet(input("what's your name\n"))
print()

# def my_function(something)          something = parameter | name of data being passed to function
# my_function(123)                    123 = argument        | value of the data passed to function

# functions with multiple inputs

def greet_with_name_and_location(name, location):
    print(f"hello {name}")
    print(f"how's the weather in {location}?")

greet_with_name_and_location("sean", "york")                        # positional arguments
greet_with_name_and_location(location = "york", name = "sean")      # keyword arguments         <-- same output
