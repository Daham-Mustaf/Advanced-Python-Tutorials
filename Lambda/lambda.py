# Write a function that takes in a list of numbers and a lambda function, and 
# returns a new list where each element in the original list has been transformed by the lambda function.

def transform_list(numbers, func):
    return [func(num) for num in numbers]

# Define the lambda function to square a number
square = lambda x: x**2

# Use the transform_list function to apply the lambda function to a list of numbers
numbers = [1, 2, 3]
transformed_numbers = transform_list(numbers, square)

print(transformed_numbers) # Output: [1, 4, 9]

# Write a function that takes in a list of strings and a lambda function, and 
# returns a new list where each element in the original list has been transformed by the lambda function.
def transform_strings(strings, lambda_fn):
    """
    Applies a lambda function to each string in a list of strings, and returns a new list with the transformed values.
    """
    transformed_strings = []
    for string in strings:
        transformed_strings.append(lambda_fn(string))
    return transformed_strings
strings = ['apple', 'banana', 'cherry']
transformed_strings = transform_strings(strings, lambda x: x.upper())
print(transformed_strings)
# Output: ['APPLE', 'BANANA', 'CHERRY']


# Write a function that takes in two lists of numbers and 
# returns a new list where each element is the sum of the corresponding elements in the input lists.

def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

add_list= add_lists([1, 2, 3], [4, 5, 6])

# Write a function that takes in a list of tuples, where each tuple contains two elements, and returns a new list where each tuple has been sorted based on the second element.
def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_tuples_list = sort_tuples(tuples_list)
print(sorted_tuples_list)  # [(1, 'banana'), (2, 'cherry'), (3, 'apple')]


# function is used to sort the list of points based on the second element of each tuple (i.e., the y-coordinate). 
points = [(2, 5), (1, 8), (3, 3), (4, 7)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(3, 3), (2, 5), (4, 7), (1, 8)]


# Write a function that takes in a list of strings representing numbers in binary format, and 
# returns a list of integers representing the decimal equivalent of each binary number. 

def binary_to_decimal(binary_list):
    return list(map(lambda x: int(x, 2), binary_list))
binary_list = ['1101', '1010', '1111']
decimal_list = binary_to_decimal(binary_list)
print(decimal_list)  # Output: [13, 10, 15]
