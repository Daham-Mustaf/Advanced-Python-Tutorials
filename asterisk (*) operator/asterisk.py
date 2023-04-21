# Write a function that takes a variable number of arguments and returns the sum of all the arguments.

def sum_args(*args):
    return sum(args)


# Write a function that takes a variable number of lists and
#  returns a flattened list of all the elements.
def flatten(*args):
    # *args parameter in the function definition allows
    # the function to accept any number of arguments, 
    # which are passed as a tuple.
    result = []
    for arg in args:
        for item in arg:
            result.append(item)
    return result

# Write a function that takes a dictionary and unpacks its key-value pairs as named arguments to another function.
def my_function(name, age):
    print(f"My name is {name} and I am {age} years old.")

arg_dict = {'name': 'Alice', 'age': 25}

# unpack_and_call(my_function, arg_dict)
# Output: My name is Alice and I am 25 years old.

# Write a function that takes a list of tuples, where each tuple contains a string and a number, and sorts the list first by the string in descending order, and then by the number in ascending order.
def sort_tuples(lst):
    lst.sort(key=lambda x: (-len(x[0]), x[1]))
    return lst



sum_args(1, 2, 3, 4)

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
result = flatten(list1, list2, list3)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = [("ccc", 3), ("bb", 2), ("a", 1), ("dddd", 4)]
sorted_lst = sort_tuples(lst)
print(sorted_lst)



