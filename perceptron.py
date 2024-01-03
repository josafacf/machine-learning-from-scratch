import math

class Perceptron:
    def __init__(self):
        # Defines the learning rate
        self.learning_rate = 0.01
        # Initializes the weights
        self.weights = [0, 0, 0]
        # Initializes the bias
        self.bias = 0.0

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def predict(self, inputs):
        # Calculates the weighted sum of the inputs
        summation = self.bias + sum(input * weights for input, weights in zip(inputs, self.weights))
        print(summation)
        # Applies the activation function
        output = self.sigmoid(summation)
        print(output)
        # If the hit rate is
        # above 0.5 return 1
        if output >= 0.5:
            return 1
        else:
            return 0

    def train(self, data, goals, epochs):
        # Loop for the number of epochs
        for _ in range(epochs):
            # Loop for each input data
            for inputs, goal in zip(data, goals):
                # Makes a prediction
                prediction = self.predict(inputs)
                # Calculates the error
                error = goal - prediction
                # Updates the bias adjusting the model
                # in learning at each interaction
                self.bias += self.learning_rate * error
                print(f'Bias: {self.bias}')

                # Loop for each input
                for i, input in enumerate(inputs):
                    # Updates the weights
                    self.weights[i] += self.learning_rate * error * input

if __name__ == "__main__":
    # Input data
    data = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0],
            [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    # Corresponding goals
    goal = [0, 0, 0, 0, 1, 1, 1, 1]

    # Creates an instance of the Perceptron class
    perceptron = Perceptron()
    # Trains the perceptron
    perceptron.train(data, goal, 100)

    print("Predictions:")
    '''
        Predictions OR:
        0 0 : 0
        1 0 : 0
        0 1 : 0
        0 0 : 0
        1 1 : 1
        1 0 : 1
        0 1 : 1
        1 1 : 1
    '''
    # Loop for each input data
    for inputs in data:
        # Makes a prediction
        prediction = perceptron.predict(inputs)
        # Prints the prediction
        print(f"{inputs[0]} {inputs[1]} : {prediction}")
