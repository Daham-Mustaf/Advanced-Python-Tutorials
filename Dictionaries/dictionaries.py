# 1 Write a function that takes in a list of dictionaries,
#  where each dictionary represents a person with keys "name" and "age". 
# The function should return the name of the oldest person.

def oldest_person(people):
    max_age = 0
    oldest_name = None
    for person in people:
        if person["age"] > max_age:
            max_age = person["age"]
            oldest_name = person["name"]
    return oldest_name

# Write a function that takes in a dictionary where the keys are strings and the values are integers. 
# The function should return the key with the highest value.
def find_key_with_highest_value(d):
    max_key = max(d, key=d.get)
    return max_key


# Write a function that takes in a list of dictionaries, where each dictionary represents a student with keys "name" and "grades". 
# The grades value is a list of integers representing the student's grades in a course. The function should return the average grade for the entire class.
def class_average(students):
    total_grades = 0
    num_students = len(students)
    for student in students:
        total_grades += sum(student['grades'])
    return total_grades / (num_students * len(student['grades']))

# Write a function that takes in a list of dictionaries, where each dictionary represents a person with keys "name" and "favorite_foods". 
# The favorite_foods value is a list of strings representing the person's favorite foods.
#  The function should return a dictionary where the keys are the favorite foods and the values are lists of people who like that food

def group_by_food(people):
    food_dict = {}
    for person in people:
        name = person["name"]
        foods = person["favorite_foods"]
        for food in foods:
            if food in food_dict:
                food_dict[food].append(name)
            else:
                food_dict[food] = [name]
    return food_dict

# Write a function that takes in a dictionary where the keys are strings and the values are lists of integers. 
# The function should return a new dictionary where the keys are the same as the original,
#  but the values are the maximum value in each list
def max_values(d):
    result = {}
    for key, value in d.items():
        result[key] = max(value)
    return result


# Write a function that takes in a list of dictionaries, 
# where each dictionary represents a person with keys "name" and "friends". 
# The friends value is a list of strings representing the person's friends. 
# The function should return the name of the person with the most friends.
def most_friends(people):
    max_friends = 0
    person_with_most_friends = ""
    for person in people:
        num_friends = len(person['friends'])
        if num_friends > max_friends:
            max_friends = num_friends
            person_with_most_friends = person['name']
    return person_with_most_friends



# ##############
people = [
    {"name": "Alice", "age": 32},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
oldest = oldest_person(people)
print(oldest)  # "Charlie"

my_dict = {"a": 10, "b": 20, "c": 5}
max_key = find_key_with_highest_value(my_dict)
print(max_key)  # prints "b"

students = [
    {'name': 'Alice', 'grades': [90, 85, 95]},
    {'name': 'Bob', 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'grades': [95, 85, 90]}
]

average = class_average(students)
print(average)

people = [
    {"name": "Alice", "favorite_foods": ["pizza", "pasta", "salad"]},
    {"name": "Bob", "favorite_foods": ["pizza", "burger", "tacos"]},
    {"name": "Charlie", "favorite_foods": ["pasta", "salad", "tacos"]},
    {"name": "David", "favorite_foods": ["pasta", "burger"]},
    {"name": "Eve", "favorite_foods": ["salad", "tacos"]}
]

food_dict = group_by_food(people)
print(food_dict)

my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
result_dict = max_values(my_dict)
print(result_dict)  # prints {'a': 3, 'b': 6, 'c': 9}


people = [
    {'name': 'Alice', 'friends': ['Bob', 'Charlie', 'Dave']},
    {'name': 'Bob', 'friends': ['Alice', 'Eve']},
    {'name': 'Charlie', 'friends': ['Alice', 'Eve', 'Mallory']},
    {'name': 'Dave', 'friends': ['Alice', 'Bob', 'Charlie', 'Eve']},
    {'name': 'Eve', 'friends': ['Bob', 'Charlie', 'Dave']},
    {'name': 'Mallory', 'friends': ['Charlie']}
]

most_friends_name = most_friends(people)
print(f"The person with the most friends is {most_friends_name}")
