# Write a function that takes in a string and returns the string with the first letter of each word capitalized.
def capitalize_first_letters(string):
    # The split() method splits the string into words using whitespace as the delimiter.
    # The list comprehension iterates over each word in the resulting list and calls the capitalize() method to capitalize the first letter. 
    # Finally, the join() method is used to combine the capitalized words into a single string with spaces between them.
    return ' '.join([word.capitalize() for word in string.split()])



# Write a function that takes in a string and returns
#  a new string with all the vowels removed.

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join(c for c in s if c not in vowels)

# Write a function that takes in a string and 
# returns the length of the longest substring that contains no repeated characters.
def longest_substring_without_repeats(s: str) -> int:
    """
    Returns the length of the longest substring that contains no repeated characters.
    """
    max_len = 0  # keep track of the maximum length seen so far
    start = 0  # start of the current substring
    chars = {}  # dictionary to store the index of the last occurrence of each character
    for i in range(len(s)):
        if s[i] in chars and chars[s[i]] >= start:
            # if the character is already in chars and its last occurrence is within the current substring
            # update the start of the current substring to be after the last occurrence of the character
            start = chars[s[i]] + 1
        else:
            # if the character is not in chars or its last occurrence is outside the current substring
            # update the maximum length seen so far
            max_len = max(max_len, i - start + 1)
        # update the index of the last occurrence of the character in chars
        chars[s[i]] = i
    return max_len


# Write a function that takes in a string and returns a new string with all the words in reverse order.
def reverse_words(string):
    # split the string into words
    words = string.split()
    # reverse the order of the words
    words.reverse()
    # join the words back into a string
    reversed_string = ' '.join(words)
    return reversed_string

# Write a function that takes in a string and returns the most common letter in the string.

def most_common_letter(s):
    # Remove whitespace and convert to lowercase
    s = s.replace(' ', '').lower()
    
    # Create a dictionary to store letter frequencies
    freq = {}
    
    # Loop through each letter in the string and add to the frequency count
    for letter in s:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    # Find the letter with the highest frequency
    max_letter = ''
    max_freq = 0
    for letter in freq:
        if freq[letter] > max_freq:
            max_letter = letter
            max_freq = freq[letter]
    
    return max_letter

# Write a function that takes in a string and returns 
# the number of times each letter appears in the string as a dictionary.
def count_letters(string):
    # Create an empty dictionary to store the count of each letter
    letter_count = {}

    # Loop through each character in the string
    for char in string:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to lowercase to ignore case sensitivity
            char = char.lower()
            # If the character is already in the dictionary, increment its count
            if char in letter_count:
                letter_count[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                letter_count[char] = 1

    # Return the dictionary of letter counts
    return letter_count

# Write a function that takes in a string and 
# returns a new string with every other character removed.
def remove_every_other(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]
    return new_string

# Write a function that takes in a string and 
# returns a new string with the first and last characters removed.

def remove_first_last_chars(s):
    return s[1:-1]

# Write a function that takes in a string and 
# returns True if the string is a palindrome, and False otherwise.

def is_palindrome(s):
    # Remove all non-alphanumeric characters from the string
    s = ''.join(filter(str.isalnum, s)).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Write a function that takes in a string and returns the number of words in the string.
def count_words(string):
    words = string.split()
    return len(words)




string = "the quick brown fox"
capitalized_string = capitalize_first_letters(string)
print(capitalized_string) # Output: "The Quick Brown Fox"


s = "Hello world! This is a test."
print(remove_vowels(s)) # Output: "Hll wrld! Ths s  tst."
s = "abcabcbb"
print(longest_substring_without_repeats(s))  # Output: 3

string = 'Hello world, how are you?'
reversed_string = reverse_words(string)
print(reversed_string)  # Output: 'you? are how world, Hello'

s = 'Hello World'
print(most_common_letter(s)) # Output: 'l'


string = "The quick brown fox jumps over the lazy dog"
letter_count = count_letters(string)
print(letter_count)

s = "hello world"
remove_every_other(s)
new_s = remove_first_last_chars(s)
print(new_s)  # Output: "ello worl"
is_palindrome(s) # Output: False
count_words(s) # Output: 2


