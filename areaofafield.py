import math

length = input("provide the length of your property in feet: ")
width = input("provide the width of your property in feet: ")

length = int(length)
width = int(width)

area = length * width

# square feet change into acre
your_acres = area / 43560
your_acres = str(your_acres)

# # concatenation example
print("Your area is: " + your_acres + " acres squared")
