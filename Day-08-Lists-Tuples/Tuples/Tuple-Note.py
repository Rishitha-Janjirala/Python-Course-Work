# Tuples
# A tuple is an ordered, immutable collection that stores multiple values in one variable. Tuples are commonly written with parentheses, and can also be created with tuple().

# Tuple properties
# - Ordered: preserves insertion order.
# - Immutable: tuple entries cannot be reassigned, added, or removed directly.
# - Iterable: can be traversed using loops.
# - Duplicates allowed: repeated values are permitted.
# - Heterogeneous: can contain multiple data types.
# - Nested structures: can contain tuples, lists, sets, and dictionaries.
# - Mutable objects inside tuples: an embedded list can still be changed.
# - Efficiency: tuples often use less memory than comparable lists; performance depends on the operation.


#Tuple operations
# Concatenation
print((1, 2) + (3, 4))            # (1, 2, 3, 4)

# Repetition
print((1, 2) * 3)                 # (1, 2, 1, 2, 1, 2)

# Indexing
data = (10, 20, 30, 40, 50)
print(data[0])                    # 10
print(data[-1])                   # 50

# Slicing: tuple[start:end:step]
print(data[1:4])                  # (20, 30, 40)
print(data[::-1])                 # (50, 40, 30, 20, 10)

# Membership
print(20 in data)                 # True
print(100 not in data)            # True



# Built-in functions for tuples
nums = (3, 1, 2)
print(len(nums))                   # 3
print(max(nums))                   # 3
print(min(nums))                   # 1
print(sum(nums))                   # 6
print(sorted(nums))                # [1, 2, 3] (a list)
print(tuple("abc"))                # ('a', 'b', 'c')
print(any((0, 0, 1)))              # True
print(all((1, 2, 3)))              # True



# Tuple methods
# Tuples have only two standard methods:
nums = (10, 20, 20, 30)
print(nums.count(20))             # 2
print(nums.index(20))             # 1


# Tuple packing and unpacking
# Packing
values = 10, 20, 30
print(values)                     # (10, 20, 30)

# Unpacking
a, b, c = values
print(a)                          # 10
print(b)                          # 20
print(c)                          # 30


# Nested tuples
data = ((1, 2), (3, 4))
print(data[0])                    # (1, 2)
print(data[1][1])                 # 4

# Tuple immutability
data = (10, 20, 30)
# data[0] = 100                  # TypeError: tuple does not support item assignment

# Mutable objects inside tuples
data = (10, [20, 30], 40)
data[1].append(50)                # Allowed: the inner list is mutable
print(data)                       # (10, [20, 30, 50], 40)
# data[0] = 100                  # Not allowed