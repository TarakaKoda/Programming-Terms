# First-Class Functions:
# "A programming language is said to have first-class function if it treats function as fist-class citizens."

# First-Class Citizen (Programming): "A first-class citizen  (sometimes called first-class objects) in a programming
# language is an entity which supports all the operations generally available to other entities. These operations
# typically include being passed as an argument, returned from a function, and assigned to a variable."

# In Python, a first-class function is a function that can be treated as a value, just like any other data type such
# as an integer or a string. Specifically, a first-class function can be:

# 1. Assigned to a variable
# 2. Passed as an argument to another function
# 3. Returned as a value from a function

# "This means that functions in Python are not just pieces of code that execute when called, but they are also objects
# that can be manipulated and passed around like any other data type. This feature is particularly useful when
# working with higher-order functions, which are functions that take one or more functions as arguments or return a
# function as their result."

# Here's an example of a first-class function in Python:
def greet(name):
    return "Hello, " + name


# Assigned the function to a variable
greeting_function = greet
print(greeting_function("srinu"))


# Passing as an argument to another function
def call_function(fun):
    return fun("pavan")


result = call_function(greet)
print(result)


# returning as a value from a function
def return_as_value():
    return greet


return_function = return_as_value()
print(return_function("naruto"))

########################################################################################################################

# Basic Example
# assign function to a variable
def square(a):
    return a*a


f = square
print(f(5))


# passing as an argument to another function
def call_fun(fun):
    return fun(5)


print(call_fun(f))


# returning as a value from a function
def return_fun():
    return f


result = return_fun()
print(result(5))

########################################################################################################################

# Creating a built-in functions such as map, filter
numbers = [x for x in range(1, 11)]
# map function for multiplication expression
example = list(map(lambda a: a * a, [1, 2, 3, 4, 5, 6, 7]))


# print(example)


def square(num):
    return num * num


def map_function(fun, list_of_numbers):
    my_list = []
    for i in list_of_numbers:
        my_list.append(fun(i))
    return my_list


my_map = map_function(square, numbers)


# print(my_map)


# filter function
def even(num):
    if num % 2 == 0:
        return num


def odd(num):
    if num % 2 != 0:
        return num


def filter_function(fun, list_of_numbers):
    result_list = []
    for num in list_of_numbers:
        result_list.append(fun(num))
    return [x for x in result_list if x is not None]


even_number = filter_function(even, numbers)
odd_number = filter_function(odd, numbers)
print(even_number)
print(odd_number)


# reduce
def reduce_fun(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


print(reduce_fun([x for x in range(1,6)]))

########################################################################################################################

# Advance Example:

def logger(message):
    def logger_message():
        print(f"{message} srinu")
    return logger_message()


message = logger("Hello")

def html_tag(tag):
    def html_wrap(message):
        print(f"<{tag}>{message}<\\{tag}>")
    return html_wrap


print_h1 = html_tag("h1")
print_h1("Hello World")
print_h1("this is me")

print_p1 = html_tag("p1")
print_p1("this is a new paragraph")



