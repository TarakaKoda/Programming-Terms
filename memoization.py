# MEMOIZATION:
# "Memoization is an optimization technique used primarily to speed up computer programs by storing the result of
# expensive function calls and returning the cached result when the same inputs occur again."

import time


def expensive_function(num):
    start_time = time.time()
    print(f"cumputing {num}....")
    time.sleep(1)
    result = num * num
    end_time = time.time()
    return f"{result}\n{int(end_time + start_time)}"



# result = expensive_function(2)
# print(result)
#
# result = expensive_function(6)
# print(result)
#
# result = expensive_function(8)
# print(result)


ef_dict = {}

def expensive_funcion(num):
    if num in ef_dict:
        return ef_dict[num]
    else:
        print(f"computing {num}...")
        time.sleep(1)
        result = num * num
        ef_dict[num] = result
        return result


result = expensive_funcion(2)
print(result)

result = expensive_funcion(6)
print(result)

result = expensive_funcion(2)
print(result)

result = expensive_funcion(6)
print(result)

# Define a function to be memoized
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Define a memoization function to cache the results of fibonacci function
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n in (0, 1):
        memo[n] = n
    else:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return memo[n]

# Test the functions
print(fibonacci(10)) # Output: 55
print(fibonacci_memo(10)) # Output: 55

