"""
This file/program is about More Variable and Printing

Like Strings

"""

name = 'Prashanth Gaddam'
age = 28 # not a lie
height = 66 # inches
weight = 128 # pounds
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} kgs heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")


#this line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.")


my_weight_in_kgs = weight / 2.2046
total = round(my_weight_in_kgs)
print(f"My weight is {total} in Kilograms.")

print(f"My weight in Kilograms is {total}")
