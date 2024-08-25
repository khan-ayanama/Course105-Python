# a frozen set is an immutable version of a set. A set is an unordered collection of unique elements, and a frozen set takes this concept a step further by ensuring that its elements cannot be modified after creation. This can be useful in scenarios where you want to create a collection of unique elements that remains constant throughout the program's execution.

# Creating a Frozen Set:
my_frozen_set = frozenset([1, 2, 3, 4, 5])


# Operations on Frozen Sets:
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])

intersection = set1.intersection(set2)
union = set1.union(set2)
difference = set1.difference(set2)
print("difference is ",difference)


# Accessing Elements:
if 3 in my_frozen_set:
    print("3 is in the frozen set")

# print(my_frozen_set(2))   # You can't print frozen set

# Hashing:
# Frozen sets are hashable, which means they can be used as keys in dictionaries and elements in other sets.
my_dict = {my_frozen_set: "value"}

