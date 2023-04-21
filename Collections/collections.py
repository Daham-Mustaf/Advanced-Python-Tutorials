# Write a function that takes in a list of integers and 
# returns the most common element.

from collections import Counter

def most_common_element(lst):
    counter = Counter(lst)
    return counter.most_common(1)[0][0]


# Write a function that takes in a list of dictionaries, where each dictionary represents a book with keys "title" and "author". The function should 
# return a dictionary where the keys are the authors and the values are lists of book titles.
def books_by_author(books):
    author_books = {}
    for book in books:
        title = book["title"]
        author = book["author"]
        if author not in author_books:
            author_books[author] = []
        author_books[author].append(title)
    return author_books

# Write a function that takes in a list of integers and 
# returns a list of all the pairs of elements that add up to 10.
def pairs_that_add_to_10(lst):
    """
    Returns a list of all the pairs of elements in lst that add up to 10.
    """
    result = []
    seen = set()
    for x in lst:
        if 10 - x in seen:
            result.append((x, 10 - x))
        seen.add(x)
    return result

# Write a function that takes in a list of integers and 
# returns a list of all the pairs of elements that have a difference of 3.
def diff_of_3(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) == 3:
                result.append((lst[i], lst[j]))
    return result


# Write a function that takes in a list of strings and 
# returns a dictionary where the keys are the first letters of each string and the values are lists of strings that start with that letter.
def group_strings_by_first_letter(strings):
    result = {}
    for s in strings:
        first_letter = s[0]
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(s)
    return result

# Write a function that takes in a list of dictionaries, where each dictionary represents a person with keys "name" and "age". The function should 
# return the name of the youngest person.
def youngest_person(people):
    youngest_age = float('inf')
    youngest_name = None
    
    for person in people:
        age = person['age']
        if age < youngest_age:
            youngest_age = age
            youngest_name = person['name']
    
    return youngest_name



lst = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6]
most_common_element(lst)

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

author_books = books_by_author(books)
print(author_books)



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(pairs_that_add_to_10(lst))
# Output: [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]

lst = ["apple", "banana", "cherry", "date", "fig", "grape", "apple pie"]
let =group_strings_by_first_letter(lst)
print(let)

people = [{'name': 'Alice', 'age': 25},
          {'name': 'Bob', 'age': 30},
          {'name': 'Charlie', 'age': 20}]

print(youngest_person(people))  # Output: Charlie
