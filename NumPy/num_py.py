# Write a function that takes a 2D NumPy array and finds the average of each row and column, and 
# returns a new array with the row and column averages as the first and last rows and columns.
import numpy as np

def row_col_averages(arr):
    row_averages = np.mean(arr, axis=1).reshape(-1, 1)
    col_averages = np.mean(arr, axis=0).reshape(1, -1)
    row_averages = np.repeat(row_averages, arr.shape[1], axis=1)
    col_averages = np.repeat(col_averages, arr.shape[0], axis=0)
    combined = np.concatenate((row_averages, arr, row_averages), axis=1)
    combined = np.concatenate((col_averages, combined, col_averages), axis=0)
    return combined

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = row_col_averages(arr)
print(result)


# Write a function that takes a NumPy array of integers 
# and returns the most common value and the frequency of that value.

def most_common_value(arr):
    unique_vals, counts = np.unique(arr, return_counts=True)
    max_count_index = np.argmax(counts)
    most_common_val = unique_vals[max_count_index]
    most_common_freq = counts[max_count_index]
    return most_common_val, most_common_freq

arr = np.array([1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])
most_common_val, most_common_freq = most_common_value(arr)
print(f"The most common value is {most_common_val} with a frequency of {most_common_freq}")



# Write a function that takes two NumPy arrays of equal length and 
# calculates the cosine similarity between them.

def cosine_similarity(a, b):
    # first compute the dot product of the two arrays using the dot function from NumPy.
    #  Then, we compute the Euclidean norms of each array using the norm function from NumPy. Finally, 
    # we divide the dot product by the product of the two norms to obtain the cosine similarity between the two arrays.
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
similarity = cosine_similarity(a, b)
print(similarity)
