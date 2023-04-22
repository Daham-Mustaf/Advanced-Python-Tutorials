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

# Write a function that takes a NumPy array and 
# applies a non-linear function (such as the sigmoid function) to each element of the array.


def sigmoid(x):
    """Apply the sigmoid function to a NumPy array"""
    return 1 / (1 + np.exp(-x))

arr = np.array([1, 2, 3, 4, 5])
result = sigmoid(arr)
print(result)

# Write a function that takes a 3D NumPy array and returns a new array where each element is the maximum value within a 2x2x2 sub-array centered around the corresponding element in the original array.
import numpy as np

def max_subarrays(arr):
    # Get dimensions of input array
    x, y, z = arr.shape
    
    # Create output array with dimensions reduced by 1 in each axis
    out = np.zeros((x-1, y-1, z-1))
    
    # Iterate over each element in the output array and find the max value in the corresponding sub-array
    for i in range(1, x):
        for j in range(1, y):
            for k in range(1, z):
                subarray = arr[i-1:i+1, j-1:j+1, k-1:k+1]
                out[i-1, j-1, k-1] = np.max(subarray)
    
    return out
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

result = max_subarrays(arr)

print(result)

# Write a function that takes a 2D NumPy array and a threshold value, and 
# returns a new array where any value greater than the threshold is replaced with the threshold value.


def threshold_array(arr, threshold):
    return np.where(arr > threshold, threshold, arr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
thresholded = threshold_array(arr, 5)
print(thresholded)

# Write a function that takes a NumPy array and returns the indices of the top k largest elements in the array.


def top_k_indices(arr, k):
    # Flatten the array and get the indices that would sort the flattened array in descending order
    sorted_indices = np.argsort(arr.ravel())[::-1]
    
    # Get the top k indices
    top_k = sorted_indices[:k]
    
    # Convert the flattened indices back to row and column indices
    row_indices, col_indices = np.unravel_index(top_k, arr.shape)
    
    # Return the row and column indices as a tuple of arrays
    return row_indices, col_indices
arr = np.array([[5, 3, 2], [9, 8, 7], [1, 4, 6]])
top_k = top_k_indices(arr, 3)
print(top_k)


