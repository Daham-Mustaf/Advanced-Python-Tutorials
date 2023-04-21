# Write a function that takes in two sets of integers and returns a new set with only the elements that are present in both sets.
def intersection_set(set1, set2):
    return set1.intersection(set2)

# Write a function that takes in a list of sets of integers and returns 
# a new set with only the elements that are present in all the sets.

def common_elements(sets):
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result &= s
    return result

# Write a function that takes in two sets of integers and
#  returns a new set with the elements that are present in the first set but not the second.
def set_difference(set1, set2):
    return set1 - set2

# Write a function that takes in a list of sets of integers and returns a 
# new set with only the elements that are present in any one of the sets but not present in all of them.

def unique_elements_in_sets(lst):
    unique_elements = set()
    common_elements = set.intersection(*lst)

    for s in lst:
        unique_elements = unique_elements.union(s)

    return unique_elements - common_elements

# Write a function that takes in two sets of strings and returns a new set with only the strings that are present 
# in the first set but not the second, ignoring case sensitivity.
def set_difference_ignore_case(set1, set2):
    """
    Returns a new set with only the strings that are present in the first set but not the second,
    ignoring case sensitivity.

    Parameters:
    set1 (set): The first set of strings.
    set2 (set): The second set of strings.

    Returns:
    set: The new set with only the strings present in the first set but not the second.
    """
    # Convert all strings in the sets to lowercase for case-insensitive comparison
    set1_lower = {s.lower() for s in set1}
    set2_lower = {s.lower() for s in set2}
    
    # Get the difference between the sets and convert all strings back to original case
    diff = {s for s in set1 if s.lower() not in set2_lower}
    
    return diff

# £££££
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result_set = intersection_set(set1, set2)
print(result_set)


sets_list = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {3, 4}]
common_elements = common_elements(sets_list)
print(common_elements)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result_set = set_difference(set1, set2)
print(result_set)


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

lst = [set1, set2, set3]
unique_elements = unique_elements_in_sets(lst)

print(unique_elements)  # prints {1, 2, 6, 7, 8, 9}


set1 = {'Apple', 'Banana', 'Orange'}
set2 = {'banana', 'kiwi', 'peach'}

diff = set_difference_ignore_case(set1, set2)
print(diff) # Output: {'Apple', 'Orange'}
