"""
The 3 apostrophes are used for multi line comment!!
+ = plus
- = minus
/ = slash
* = asterisk
% = percent
< = less-than
> = greate-than
<= = less-than-equal
>= = greater-than-equal

"""


"""
In python the order of operations are done in PEMDAS stands for Parantheses Exponents Multiplication Division Addition Subtraction
Actual order is multiplication and division in one step from left to right
then you do addition and subtraction in one step from left to right.
So PEMDAS is PE(M&D)(A&S)

"""

print("I will now count my chickens:")

# In the below line it first divides 30/6 and then adds with 25
print("Hens", 25+30/6)

# In the below line it first does multiplication 25*3 then result is modulus with 4 and then subtract
print("Roosters", 100-25*3%4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3+2<5-7?")

print(3+2<5-7)

print("what is 3+2?", 3+2)
print("What is 5-7?", 5-7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
