import itertools

# Example 1:

my_list = [1,2,3]

# combinations = itertools.combinations(my_list,2)
# for c in combinations:
#     print(c)
#
# permutations = itertools.permutations(my_list, 3)
# for p in permutations:
#     print(p)

# Example 2:
# In this case it is better to use combinations instead of permutations

# my_example_list = [x for x in range(1,7)]
#
# combinations1 = itertools.combinations(my_example_list, 3)
# permutations1 = itertools.permutations(my_example_list, 2)
#
# print([result for result in combinations1 if sum(result) == 10])

# Example 3:
# In this case it is better to use permutations instead of combinations

word = "srinu"
my_string = "unirs"

# combinations = itertools.combinations(my_string, 5)
permutations = itertools.permutations(my_string, 5)

for p in permutations:
    result = "".join(p)
    if result == word:
        print(f"matched {result}")
        break
else:
    print(f"{word} has no matches")
