# Function to update weights
def update_weights(weights, learning_rate, error, input_data):
    # Loop through each weight
    for i in range(len(weights)):
        # Update the weight
        weights[i] += learning_rate * error * input_data[i]
    # Return the updated weights
    return weights


# Initial weights
weights = [0.20, 0.10, 0.5]
# Learning rate
learning_rate = 0.1
# Input data
input_data = [1, 2, 3]
# Error value
error = 0.1

print("Initial weights:", weights)

# Update the weights 5 times
for update in range(5):
    '''
        *learning_rate = 0.01*
        Initial weights: [0.2, 0.1, 0.5]
        Weight update 1: ['0.20', '0.10', '0.50']
        Weight update 2: ['0.20', '0.10', '0.51']
        Weight update 3: ['0.20', '0.11', '0.51']
        Weight update 4: ['0.20', '0.11', '0.51']
        Weight update 5: ['0.21', '0.11', '0.52']

        *learning_rate = 0.05*
        Initial weights: [0.2, 0.1, 0.5]
        Weight update 1: ['0.21', '0.11', '0.52']
        Weight update 2: ['0.21', '0.12', '0.53']
        Weight update 3: ['0.22', '0.13', '0.55']
        Weight update 4: ['0.22', '0.14', '0.56']
        Weight update 5: ['0.23', '0.15', '0.58']

        *learning_rate = 0.1*
        Initial weights: [0.2, 0.1, 0.5]
        Weight update 1: ['0.21', '0.12', '0.53']
        Weight update 2: ['0.22', '0.14', '0.56']
        Weight update 3: ['0.23', '0.16', '0.59']
        Weight update 4: ['0.24', '0.18', '0.62']
        Weight update 5: ['0.25', '0.20', '0.65']
    '''
    # Update the weights
    weights = update_weights(weights, learning_rate, error, input_data)
    # Print the updated weights
    print(f"Weight update {update + 1}: {[f'{w:.2f}' for w in weights]}")
