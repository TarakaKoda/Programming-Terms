# Closures

# "A closure is a record storing a function together with an environment: a mapping associating each free variable of
# the function with the value or storage location to which the name was bound when the closure was created. A
# closure, unlike a plain function, allows the function to access those captured variables through the closure's
# reference to them, even when the function is defined outside their scope."

# remembers the enclosing variable
def outer_fun():
    message = "hi"

    def inner_fun():
        print(message)

    return inner_fun


my_message = outer_fun()
my_message()


# passing message as an argument
def out_fun(msg):
    message = msg
    print(message)

    def inn_fun():
        message = "hello"
        print(message)

    return inn_fun


my_fun = out_fun("hi")
my_fun()


# passing function as an  argument
def cal(fun):
    def inner_fun(*args):
        # print(f"argument that are passed are {args}")
        print(fun(*args))

    return inner_fun


def add_fun(x, y):
    return x + y


def sub_fun(x,y):
    return x - y


my_add = cal(add_fun)
my_sub = cal(sub_fun)

my_add("a", str(8))
my_add(9, 6)

my_sub(7, 2)
my_sub(9, 6)


def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))