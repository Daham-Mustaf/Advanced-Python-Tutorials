



# 1- Write a function that takes in a list of strings and returns
#  a new list with all the strings that are palindromes.
from ast import Lambda


def find_palindromes(words):
    """
    Returns a list of palindromic strings from the input list.
    """
    palindromes = []
    for word in words:
        if word == word[::-1]: # slice the entire string, but with a step of -1, so it effectively reverses the string.
            palindromes.append(word)
    return palindromes


# Write a function that takes in a list of numbers and returns a new list with all the even numbers sorted in descending order, followed by all 
# the odd numbers sorted in ascending order.
def even_odd_sort(numbers):
    evens = sorted([n for n in numbers if n % 2 == 0], reverse=True)
    odds = sorted([n for n in numbers if n % 2 == 1])
    return evens + odds



# Write a function that takes in a list of dictionaries, where each dictionary
#  represents a person with keys "name" and "age",
#  and returns a new list of dictionaries sorted by age in ascending order.

def sort_people_by_age(people_list):
    """
    Sort a list of people by age in ascending order.

    Args:
        - people_list (list): A list of dictionaries representing people, where each dictionary has keys "name" and "age".

    Returns:
        - sorted_people_list (list): A new list of dictionaries sorted by age in ascending order.
    """
    sorted_people_list = sorted(people_list, key=lambda p: p["age"])
    return sorted_people_list


# Write a function that takes in two lists of integers and returns 
# a new list with all the unique elements from both lists.

def get_unique_elements(list1, list2):
    # Merge both lists
    merged_list = list1 + list2

    # Create a set from the merged list to get unique elements
    unique_set = set(merged_list)

    # Convert the set back to a list and return
    unique_list = list(unique_set)
    return unique_list


# Write a function that takes in a list of integers and returns a new list with all the 
# sublists that have a sum greater than or equal to a given value.

def sublist_sum_greater_than(lst, val):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sub = lst[i:j]
            if sum(sub) >= val:
                result.append(sub)
    return result




words = ['racecar', 'hello', 'deified', 'world', 'level']
palindromes = find_palindromes(words)
print(palindromes)  

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = even_odd_sort(my_list)
print(sorted_numbers)

people_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
]
sorted_people_list = sort_people_by_age(people_list)
print(sorted_people_list)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
unique_elements = get_unique_elements(list1, list2)
print(unique_elements)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 10
result = sublist_sum_greater_than(lst, val)
print(result)  # [[3, 4], [4, 5], [5], [6, 7], [7, 8], [8, 9], [9]]


