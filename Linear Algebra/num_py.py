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
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = simple_neuron(inputs, weights, bias)
print(output) # Expected output: 4.8
ot_t= np.dot(inputs, weights) + bias