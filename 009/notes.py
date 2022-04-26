# dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", # put comma at the end of every line, just to make it easier to add stuff
}

# retrieve item from dictionary
print(programming_dictionary["Bug"])
print()

# add item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
print()

# create empty dictionary
empty_dictionary = {}

# wipe existing dictionary
# programming_dictionary = {}

# edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."  # if no entry with key "Bug" exists, this'll create it
print(programming_dictionary)
print()

# loop through dictionary
for key in programming_dictionary:
    print(key)                                            # just prints the key
    print(programming_dictionary[key])                    # prints the definition

########################

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# nesting a list within a list

["A", "B", ["C", "D"]]                                  # valid, but not as useful

# nesting a list within a dictionary within a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

my_travel_log = {
    "Japan": {"cities_visited": ["Tokyo","Sapporo","Utsonomaya"], "years_visited": 2015},
    "France": {"cities_visited": ["Paris","Nice","Bayeux"], "years_visited": [2009,2017,2019]},
}

print(my_travel_log["France"])

# nesting a dictionary in a list

# there's two dictionaries in this list
# they're line separated for legibility
# each dictionary has three key:value pairs
# they all have diffenet kinds of data - string, list, integer

my_travel_log_list = [
    {
        "country": "Japan", 
        "cities_visited": ["Tokyo","Sapporo","Utsonomaya"], 
        "years_visited": 2015
    },
    {
        "country": "France", 
        "cities_visited": ["Paris","Nice","Bayeux"], 
        "years_visited": [2009,2017,2019]
    },
]