# 🚨 Don't change the code below 👇
from posixpath import split
from turtle import pos


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# coordinates = position.split(", ") # turns input into a list

x = int(position[0])
y = int(position[1])

# if y == 1:
#     row1[(x-1)] = "X"
# elif y == 2:
#     row2[(x-1)] = "X"
# elif y == 3:
#     row3[(x-1)] = "X"

# map[y-1] is a better way to get the horizontal

# SUPER clean way to do it:

map[y-1][x-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")