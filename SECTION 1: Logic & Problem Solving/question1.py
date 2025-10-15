def second_largest(numbers): 
    # This function returns the second largest number in a list of integers.

    unique_numbers = list(set(numbers))
    # it removes duplicates by converting the list to a set and back to a list.
    if len(unique_numbers) < 2:
        return None
    # it returns None if the list has less than two unique numbers.
    unique_numbers.sort(reverse=True)
    # it sorts the unique numbers in descending order.
    return unique_numbers[1]

# how to use the function: start by creating a list of integers.
nums = list(range(60, 100))  
# print the list of intergers and the second largest number.
print("List:", nums)
print("Second largest number:", second_largest(nums))
