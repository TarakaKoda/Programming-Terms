# DRY stands for "Don't Repeat Yourself", which is a principle of software development that emphasizes the importance
# of avoiding duplication of code and promoting code re-usability. In Python, following the DRY principle can help you
# write more maintainable, readable, and efficient code.

# Here are some tips for applying DRY in Python:

# Use functions and classes to encapsulate reusable code: If you find yourself copying and pasting the same code in
# multiple places, it's a good sign that you should create a function or a class to encapsulate the code and make it
# reusable.

# Use constants and configuration files: If you have values that are used in multiple places in your code,
# such as API endpoints or database connection settings, you can define them as constants or in a configuration file
# to avoid repeating them throughout your code.

# Avoid hard-coding values: Instead of hard-coding values like file paths, database connection strings, or URLs,
# use variables or constants to make your code more flexible and easier to maintain.

# Use loops and list comprehensions: Instead of writing repetitive code to iterate over lists or perform the same
# operation on multiple items, use loops or list comprehensions to avoid repeating yourself.

# Use built-in functions and libraries: Python has many built-in functions and libraries that can help you avoid
# repeating yourself, such as the zip() function for iterating over multiple lists at once or the collections module
# for working with collections of data.

# By following these best practices, you can write Python code that is more concise, readable, and maintainable,
# while avoiding the pitfalls of duplication and inconsistency that can lead to errors and inefficiencies.

# Example: A program that needs to convert a list of temperatures from Celsius to Fahrenheit.

temperature_in_celsius = [23, 25, 37]
fahrenheit_temperatures = []

for temp in temperature_in_celsius:
    fahrenheit = (temp * 9/5) + 32
    fahrenheit_temperatures.append(fahrenheit)

print(fahrenheit_temperatures)

# To apply DRY, we can encapsulate the formula in a separate function and call it for each temperature in the list.


def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32


temperature_in_celsius = [23, 25, 37]
fahrenheit_temperatures = []

for temp in temperature_in_celsius:
    fahrenheit = celsius_to_fahrenheit(temp)
    fahrenheit_temperatures.append(fahrenheit)

print(fahrenheit_temperatures)

