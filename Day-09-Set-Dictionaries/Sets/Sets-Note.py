# 1. Sets

# A set is an unordered, mutable collection of unique elements.

# Properties:
# Unordered collection
# Mutable
# Does not support indexing
# Does not allow duplicate values
# Can store different data types

# Operations
# Membership (in, not in) --Checks whether an element exists.

# Union (|) --Combines all unique elements from both sets.

# Intersection (&) --Returns common elements.

# Difference (-)  --Returns elements present in the first set but not second.

# Symmetric Difference (^)  --Returns elements present in either set but not both.

# Subset (<=)  --Checks whether all elements of one set exist in another.

# Superset (>=) --Checks whether a set contains all elements of another set.


# Built-in Functions
# len(), max(), min(), sum(), sorted(), set(), any(), all()

# Set Methods
# Adding: add(), update()

# Removing: remove(), discard(), pop(), clear()

# Copying: copy()

# Set operations:
#  union(), intersection(), difference(), symmetric_difference()

# Relationship methods: issubset(), issuperset(), isdisjoint()

# Example

a = {1, 2, 3}
b = {3, 4, 5}

print(f'Union:{a | b}')
print(f'Intersection:{a & b}')
print(f'Difference:{a - b}')
print(f'Symmetric:{a ^ b}')



# 2. Frozenset

# A frozenset is an immutable version of a set. Once created, its elements cannot be added or removed.

data = frozenset({10, 20, 30})
print(data)