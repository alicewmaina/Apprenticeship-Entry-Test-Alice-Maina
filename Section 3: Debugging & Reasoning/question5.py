# given code
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)

# 1. What’s wrong with the code?

# The code tries to remove elements from the list while iterating over it using indices.
#  This causes unexpected behavior because the list changes size as you remove items, so the indices no longer match the intended elements.
# Also, numbers.remove(i) tries to remove the value i, not the value at index i. 
# Since i is an index, not necessarily a value in the list, this can cause a ValueError if i is not in numbers.


# 2. What will it output?

# It will raise an error:
# ValueError: list.remove(x): x not in list
# because, for example, when i = 4, the value 4 may no longer be in the list.



# 3. How would you fix it to remove even numbers correctly?

# Here’s a correct way to remove even numbers from the list:


numbers = [1, 2, 3, 4, 5]
for i in numbers[:]:
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)