import math


# Inputs

radius = input("provide the radius of a cylinder")
height = input("provide the height of a cylinder")

radius = float(radius)
height = float(height)

# calculate the volume of cylinder
volume = math.pi*radius*radius*height

print("volum of a cylinder will be %.1f" %volume)
