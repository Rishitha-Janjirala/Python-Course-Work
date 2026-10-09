# Lists
# A list is an ordered, mutable collection that stores multiple values in one variable. Create a list with [] or list().

# List properties
# - Ordered: preserves insertion order.
# - Mutable: elements can be modified.
# - Indexed: supports positive and negative indices.
# - Iterable: can be traversed using loops.
# - Duplicates allowed: repeated values are permitted.
# - Dynamic size: can grow or shrink.
# - Heterogeneous: can hold multiple data types.

#List operations

# Concatenation
print([1, 2] + [3, 4])            # [1, 2, 3, 4]

# Repetition
print([1, 2] * 3)                 # [1, 2, 1, 2, 1, 2]

# Indexing
values = [10, 20, 30, 40, 50]
print(values[0])                  # 10
print(values[-1])                 # 50

# Slicing: list[start:end:step]
print(values[1:4])                # [20, 30, 40]
print(values[::-1])               # [50, 40, 30, 20, 10]

# Membership
print(20 in values)               # True
print(100 not in values)          # True

#Built-in functions for lists
nums = [3, 1, 2]
print(len(nums))                   # 3
print(max(nums))                   # 3
print(min(nums))                   # 1
print(sum(nums))                   # 6
print(sorted(nums))                # [1, 2, 3]
print(list("abc"))                 # ['a', 'b', 'c']

# List methods
# Adding elements
nums = [10, 20]
nums.append(30)                   # Adds one element at the end
print(nums)                       # [10, 20, 30]

nums.extend([40, 50])             # Adds elements from an iterable
print(nums)                       # [10, 20, 30, 40, 50]

nums.insert(1, 15)                # Inserts at index 1
print(nums)                       # [10, 15, 20, 30, 40, 50]

#Removing elements
nums = [10, 20, 20, 30]
nums.remove(20)                   # Removes first matching value
print(nums)                       # [10, 20, 30]

removed = nums.pop(1)             # Removes and returns index 1
print(removed)                    # 20
print(nums)                       # [10, 30]

nums.clear()                      # Removes all elements
print(nums)                       # []

nums = [10, 20, 30]
del nums[0]                       # Deletes element at index 0
print(nums)                       # [20, 30]

# Note: del is a Python statement, not a list method. Calling pop() without an index removes the last item.
# Searching
nums = [10, 20, 10, 30]
print(nums.index(20))             # 1
print(nums.count(10))             # 2

# Sorting and reversing
nums = [30, 10, 20]
nums.sort()                       # Sorts the original list
print(nums)                       # [10, 20, 30]

nums.reverse()                    # Reverses the original list
print(nums)                       # [30, 20, 10]

print(sorted(nums))               # [10, 20, 30] (new list)
print(nums)                       # [30, 20, 10] (unchanged)

# Note: sorted() is a built-in function, while sort() is a list method.
# Copying
original = [10, 20, 30]
copied = original.copy()          # Shallow copy
print(copied)                     # [10, 20, 30]

# Nested lists
# A nested list is a list inside another list.
data = [[1, 2], [3, 4]]
print(data[0])                    # [1, 2]
print(data[1][1])                 # 4
