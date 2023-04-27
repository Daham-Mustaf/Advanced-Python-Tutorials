import numpy as np

#  wrie a function to crate a simmple neuron


def simple_neuron(inputs, weights, bias):

    # Calculate the weighted sum of the inputs
    weighted_sum = 0
    for i in range(len(inputs)):
        weighted_sum += inputs[i] * weights[i]
    
    # Add the bias to the weighted sum
    weighted_sum += bias
    
    # Apply the ReLU activation function
    output = max(0, weighted_sum)
    
    return output
# compute A Layer of Neurons 

def layer(inputs, weights, biases, activation):
    # Compute the weighted sum of the inputs
    weighted_sum = np.dot(inputs, weights) + biases
    
    # Apply the activation function
    output = activation(weighted_sum)
    
    return output

# Inputs to the layer
inputs = np.array([1.0, 2.0, 3.0])

# Weights for the layer (3 neurons with 4 inputs each)
weights = np.array([
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
])

# Biases for the layer (3 neurons)
biases = np.array([2.0, 3.0, 0.5])

# Activation function for the layer (ReLU)
def relu(x):
    return np.maximum(0, x)

# Compute the layer output
output = layer(inputs, weights, biases, relu)

# Print the output
print(output) # Expected output: [4.8 1.21 2.39]



inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = simple_neuron(inputs, weights, bias)
print(output) # Expected output: 4.8
ot_t= np.dot(inputs, weights) + bias