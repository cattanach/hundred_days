# scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()                              # prints 2
print(f"enemies outside function: {enemies}")   # prints 1


# local scope

def drink_potion():
    potion_strength = 2         # local
    print(potion_strength)

# potion_strength       won't run, undefinied outside function
drink_potion()


# global scope

player_health = 10      # global 

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)        # will run

    drink_potion()

player_health()


# python doesn't have block scope

if 3 > 2:
    a_variable = 10

game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # this is valid

game_level = 3
def create_enemy():
    enemies = ["skeleton", "zombie", "alien"]
    if game_level < 5:
        new_enemy = enemies[0] 

# print(new_enemy)          # this isn't valid
    print(new_enemy)        # but this is


# modifying global scope

enemies = 1

def increase_enemies():
  global enemies    # this pulls from the global variable above
  enemies = 2       # creating a new enemies variable
  print(f"enemies inside function: {enemies}")

increase_enemies()                              # prints 2
print(f"enemies outside function: {enemies}")   # prints 1

# generally speaking, bad idea to call local and global variables the same thing
# probably don't want to modify things with global scope either

# alternatively, you can do this:

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()                    # prints 2
print(f"enemies outside function: {enemies}")   # prints 1


# global constants
# totally kosher if it's something you're not going to change
# naming convention is to use all uppercase

PI = 3.14159 # for example
URL = "https://example.com"

