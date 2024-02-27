import random
import math

# Setting the seed for the random number generator
random.seed(0)

# Number of hidden layers in the neural network
num_hidden_layers = 3
# Number of neurons in each hidden layer
neurons_per_layer = [10, 5, 2]

# Initialization of weights
def initialize_weights(num_input_neurons, num_output_neurons):
    # Create a weight matrix with random values between -1 and 1
    return [[random.uniform(-1, 1)
             for _ in range(num_output_neurons)]
            for _ in range(num_input_neurons)]

# Store  the weights of the
# connections between the neurons
weights = []
# Number of neurons in the input layer
input_neurons = 15
# Number of neurons in the output layer
output_neurons = 1

# Initializes the weights of
# the connections between the layers of neurons
weights.append(initialize_weights(
    input_neurons, neurons_per_layer[0]))
for i in range(num_hidden_layers - 1):
    weights.append(initialize_weights(
        neurons_per_layer[i],
        neurons_per_layer[i+1]))
weights.append(initialize_weights(
    neurons_per_layer[-1], output_neurons))

# Data Propagation
def sigmoid(x):
    # Sigmoid activation function(0, 1)
    return 1 / (1 + math.exp(-x))

def propagate_date(input_data):
    # Propagetes the input data throught the network
    signals = input_data
    for layer in weights:
        new_signals = []
        for i in range(len(layer[0])):
            # Calculate sthe new_signals from layeres
            s = sum(layer[j][i] * signals[j] for j in range(len(signals)))
            new_signals.append(sigmoid(s))
        signals = new_signals
    return signals

# Calculation of the network output
def network_output(input_data):
    # Calculates the output of the
    # network for a given set of input data
    return propagate_date(input_data)

# Test of the new neural network
test_data = [0.5, 0.3,
             0.8, 0.2, 0.1, 0.9, 0.4, 0.6,
             0.7, 0.2, 0.5, 0.3, 0.8, 0.2, 0.1]
predicted_output = network_output(test_data)
print("Predicted output: ", predicted_output)
