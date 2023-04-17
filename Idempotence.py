# Idempotence:
# Idempotence can be achieved by writing functions or methods that perform the same action every time
# they are called with the same arguments.

# Example 1:
def square(x: int) -> int:
    return x * x


print(square(2))
print(square(2))

# In this example, the square function takes a number x and returns its square. If we call square(2) once,
# we get the result 4. If we call it again with the same argument, we will get the same result, 4, without any
# unexpected side effects.

# Example 2:
my_set = {1, 2, 3}

my_set.add(4)  # Still my_set = {1, 2, 3, 4}
my_set.add(4)  # Still my_set = {1, 2, 3, 4}
print(f"{my_set = }")

# The use of set operations. For instance, adding an item to a set is idempotent, as adding the same item multiple
# times will not change the set beyond the initial addition.

# Practical example:
# Idempotence are used in HTTP methods:
# GET - Idempotent  <url>/users/123 -> It will give you the same result no matter how many times you call it.
# PUT - Idempotent  Updating values -> You update same parameter to the same value everytime it will give you the same result.
# POST - NOT Idempotent -> It is used for changing data in the background.
# DELETE - Idempotent -> Once you delete the state of the server will remain the same no matter how many times you call it .
