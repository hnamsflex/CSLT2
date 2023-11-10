# Exercise 37: Name that Shape

# (Solved—31 Lines)
# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.


sides = int(input("Enter the number of sides:"))
shape = ""
if sides < 3 or sides > 10:
    print("Error")
else:
    if sides == 3:
        shape = "triangle"
    elif sides == 4:
        shape = "quadrilateral"
    elif sides == 5:
        shape = "pentagon"
    elif sides == 6:
        shape = "hexagon"
    elif sides == 7:
        shape = "heptagon"
    elif sides == 8:
        shape = "octagon"
    elif sides == 9:
        shape = "nonagon"
    elif sides == 10:
        shape = "decagon"
    print(f"A shape with {sides} sides is called a {shape}.")