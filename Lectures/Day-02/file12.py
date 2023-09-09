# Hashing is a fundamental concept in computer science and plays a crucial role in data structures like frozen sets, as well as dictionaries and other hash-based collections. Hashing is used to efficiently retrieve and store data in a way that allows for quick lookups and comparisons.

# Here's an explanation of hashing in the context of frozen sets:

# Hashing:
# Hashing is a process of mapping data (such as objects, values, or keys) to a fixed-size value or hash code. The hash code is typically an integer, and it's calculated using a hashing function. The purpose of hashing is to quickly identify a location where the data can be stored or retrieved in a data structure, such as an array or a hash table.

# Hashing in Frozen Sets:
# In the case of frozen sets, hashing is used to efficiently store and retrieve elements from the set. When you create a frozen set, each element in the set is assigned a hash code based on its value. This hash code is used to determine the element's position in memory or in a hash table-like structure. The hash code allows for quick access to elements without having to iterate through the entire collection.

# Key Properties of Hashing:

# Deterministic: The same element will always produce the same hash code, allowing for consistent lookups and retrievals.

# Fast Retrieval: Hashing allows for constant-time average-case retrieval, meaning that accessing an element's value is very efficient.

# Uniqueness: Different elements should ideally produce different hash codes to avoid collisions (multiple elements mapping to the same hash code).

# Avalanche Effect: A small change in the input data should result in a significantly different hash code, distributing elements uniformly.

# Example:
# Let's say you have a frozen set f_set = frozenset([10, 20, 30]). Each of the elements, 10, 20, and 30, would have its own hash code calculated using a hashing function. These hash codes are then used to determine where these elements are stored in memory, allowing for efficient access.

# Hashing plays a crucial role in the performance of hash-based data structures, like frozen sets and dictionaries. It ensures that data can be accessed and manipulated quickly, even when dealing with large collections, by enabling direct addressing and reducing the need for linear searches through the entire collection.

# Create a frozen set
fruits = frozenset(["apple", "banana", "orange"])

# Hash codes for the elements in the frozen set
hash_code_apple = hash("apple")
hash_code_banana = hash("banana")
hash_code_orange = hash("orange")

# Demonstrate hash codes
print("Hash code for 'apple':", hash_code_apple)
print("Hash code for 'banana':", hash_code_banana)
print("Hash code for 'orange':", hash_code_orange)

# Simulating a hash-based data structure for retrieval
hash_table = {
    hash_code_apple: "apple",
    hash_code_banana: "banana",
    hash_code_orange: "orange"
}

# Retrieve elements using hash codes
element_to_retrieve = "banana"
element_hash = hash(element_to_retrieve)
if element_hash in hash_table:
    retrieved_element = hash_table[element_hash]
    print("Retrieved:", retrieved_element)
else:
    print("Element not found")

# Trying to retrieve a non-existent element
non_existent_element = "grape"
non_existent_element_hash = hash(non_existent_element)
if non_existent_element_hash in hash_table:
    retrieved_element = hash_table[non_existent_element_hash]
    print("Retrieved:", retrieved_element)
else:
    print("Element not found")
