# String Interpolation:
# String interpolation in Python is the process of embedding a variable's value or expression inside a string.
# There are several ways to perform string interpolation in Python, including using:
# 1. The % operator
# 2. The str.format() method
# 3. Using an f-strings.

# Example 1: Using % operator
name = "srinu"
age = 22

result = "Example 1: My name is %s and i'm %d years old." % (name, age)
print(result)

# Example 2: Using the formatted string

name = "srinu"
age = 22

result = "Example 2.1: My name is {} and i'm {} years old".format(name, age)
print(result)

result = "Example 2.2: My name is {name} and i'm {age} years old".format(age=age, name=name)
print(result)

# Example 3: Using f-strings

name = "srinu"
age = 22

result = f"Example 3: My name is {name} and i'm {age} years old."
print(result)
