# MUTABLE DATA TYPES:
# List: my_list = [0,2,3,4,5,6,7,8,9..]
# Dictionary: my_dict = {"name": "srinu", "age": 22, "city": "vizag"..}
# Set: my_set = {1,3,4,a,g,j,h,r,e,6,7,8,9..}
# Byte Array:

# IMMUTABLE DATA TYPES:
# Integer: number = 42
# Float: float_num = 45.2
# Complex: cmp_num = 2 + 3j
# String: my_name = "srinu"
# Tuple: my_tuple = (1,2,3,4,5,6,7,8,9)
# Frozenset: fruits = frozenset(["apple", "mango", "banana"])

# string is an immutable
a = "srinu"
print(a)
print(f"Address of a is: {id(a)}")
a ="pavan"
print(a)
print(f"Address of a is: {id(a)}")

# a[0] = "C" # this gives an error


# List is mutable

my_list = [x for x in range(5)]
print(my_list)
print(f"Address of my_list: {id(my_list)}")
my_list[0] = 1
print(my_list)
print(f"Address of my_list: {id(my_list)}")

