import math

# tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

# sigmoid(x) = 1 / (1 + exp(-x))
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# def relu(x):
#    if x < 0:
#        return 0
#    else:
#        return x
def relu(x):
    return max(0, x)

# f(x) = max(alpha * x, x)
def leakyRelu(x, alpha=0.01):
    return max(alpha*x, x)

# binary_step(x) = 1 se x for maior ou igual a 0, senão 0.
def binaryStep(x):
    return 1 if x >= 0 else 0

# Array to test
x = [-1, 8]

for num in x:
    '''
        Hyperbolic Tangent: -0.7615941559557649
        Sigmoid: 0.2689414213699951
        Relu: 0
        Leaky Relu: -0.01
        Binary Step: 0
        ------------------------------
        Hyperbolic Tangent: 0.999999774929676
        Sigmoid: 0.9996646498695336
        Relu: 8
        Leaky Relu: 8
        Binary Step: 1
        ------------------------------
    '''
    # Hyperbolic Tangent can return values between -1 and 1
    print("Hyperbolic Tangent:", tanh(num))
    # Sigmoid returns values between 0 and 1
    print("Sigmoid:", sigmoid(num))
    # Relu can return 0 as well as positive values
    print("Relu:", relu(num))
    # Leaky ReLU returns the input value if it is greater than zero
    # or equal to zero or negative values
    print("Leaky Relu:", leakyRelu(num))
    # Returns a binary value of 0 or 1
    print("Binary Step:", binaryStep(num))
    print("------------------------------")