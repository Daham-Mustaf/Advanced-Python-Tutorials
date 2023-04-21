# Write a function that takes in a list of tuples and returns 
# a new list with only the tuples that have a length greater than or equal to 2.

def filter_tuples(lst):
    """
    Filters a list of tuples based on the length of each tuple.
    """
    return [t for t in lst if len(t) >= 2]


# Write a function that takes in a list of tuples, where each tuple represents a 
# student's name and their grades for a course. The function should return a new list 
# of tuples where each tuple contains the student's name and their average grade.
def calculate_average_grades(students):
    """
    Calculates the average grade for each student and returns a new list of tuples.

    Args:
        students (list of tuples): List of tuples where each tuple contains the student's name and their grades.

    Returns:
        List of tuples where each tuple contains the student's name and their average grade.
    """
    results = []
    for name, grades in students:
        avg_grade = sum(grades) / len(grades)
        results.append((name, avg_grade))
    return results

# Write a function that takes in a list of tuples, where each tuple contains a string and a number.
#  The function should return a new tuple where the string is concatenated with the number as a string.
def concatenate_tuples(lst):
    new_lst = []
    for tup in lst:
        new_tup = (tup[0] + str(tup[1]),)
        new_lst.append(new_tup)
    return new_lst

# Write a function that takes in a list of tuples, where each tuple contains a name and an age. 
# The function should return a new list of tuples where each tuple contains the name and the age increased by 1.
def increase_age(lst):
    return [(name, age + 1) for name, age in lst]


# Write a function that takes in a list of tuples, where each tuple contains a string and a list of integers.
#  The function should return a new list of tuples where each tuple contains the original string and the sum of the integers in the list.

def sum_tuples(lst):
    new_lst = []
    for tup in lst:
        string, ints = tup
        total = sum(ints)
        new_tup = (string, total)
        new_lst.append(new_tup)
    return new_lst

# Write a function that takes in a list of tuples, where each tuple contains a string and a dictionary. 
# The dictionary represents a set of key-value pairs where the keys are strings and the values are integers. The function should return a new list of tuples where each tuple contains the original string and the sum of the values in the dictionary.
def sum_values_in_dict(lst):
    result = []
    for tup in lst:
        s = sum(tup[1].values())
        result.append((tup[0], s))
    return result



lst = [(1, 2), (3,), (4, 5, 6), (), (7, 8)]
filtered_lst = filter_tuples(lst)
print(filtered_lst) # [(1, 2), (4, 5, 6), (7, 8)]

students = [("Alice", [90, 85, 95]), ("Bob", [80, 75, 70]), ("Charlie", [95, 92, 98])]
results = calculate_average_grades(students)
print(results) # [("Alice", 90.0), ("Bob", 75.0), ("Charlie", 95.0)]

lst = [('hello', 42), ('world', 123), ('foo', 7)]
new_lst = concatenate_tuples(lst)
print(new_lst)
# [('hello42',), ('world123',), ('foo7',)]


people = [("Alice", 23), ("Bob", 30), ("Charlie", 18)]
new_people = increase_age(people)
print(new_people)

lst = [("a", [1, 2, 3]), ("b", [4, 5, 6]), ("c", [7, 8, 9])]
new_lst = sum_tuples(lst)
print(new_lst)  # Output: [("a", 6), ("b", 15), ("c", 24)]

data = [("John", {"math": 80, "science": 90, "history": 75}),        ("Jane", {"math": 95, "science": 85, "history": 80}),        ("Bob", {"math": 70, "science": 80, "history": 90})]
result = sum_values_in_dict(data)
print(result)
