# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.

# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(new_country, new_visits, new_cities):
    travel_log.append({
        "country": new_country,
        "visits": new_visits,
        "cities": new_cities
    })


    # OR


# def add_new_country(new_country, new_visits, new_cities):
#     new_country_dict = {}
#     new_country_dict["country"] = new_country
#     new_country_dict["visits"] = new_visits
#     new_country_dict["cities"] = new_cities
#     travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
