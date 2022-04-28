# functions with outputs

def my_function():
    '''Doesn't do anything interesting'''
    result = 3 * 2
    return result

output = my_function()

print(output)

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    # nothing after return gets run
    print("this won't print")

print(format_name("teD", "DANsoN"))

# multiple return values

def format_name_again(f_name, l_name):
    """Takes a first and last name and puts it in title case.
    You can write these on multiple lines"""                    # docstring
    if f_name == "" or l_name == "":
        return f"No input"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name_again(input("What is your first name? "), input("What is your surname? ")))

# a = 5, which means c = 5. b = 10, which means d = 10. 
# The output of inner_function becomes the output of outer_function.

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)



def outer_function():
    print("I'm outer")
    def nested_function():
        print("I'm inner")
    def one():
        print("one")
    def two():
        print("two")
    return nested_function, one, two
 
inner_function, a, b = outer_function()
inner_function(), b()