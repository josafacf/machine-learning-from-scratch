# p(A|B) = p(B|A) * p(A) / p(B)
# josafa_dev
def calc(probability_b_given_a, probability_a, probability_b):
    probability_a_given_b = (probability_b_given_a * probability_a) / probability_b
    return probability_a_given_b

# weights=> P(B|A) |P(A) |P(B)
data = [(   0.8,   0.5,  0.6), (0.7, 0.4, 0.5), (0.9, 0.3, 0.7)]

# calculate the probability of a to b => P(A|B) 
results = [calc(probability_b_given_a, probability_a, probability_b) 
           for probability_b_given_a, probability_a, probability_b in data]

# Show Results
'''
Sun: 66.67%
Sun: 56.00%
Rain:  38.57%
'''
for i, result in enumerate(results):
    if (result <= 0.50):
        print(f"Rain:  {result*100:.2f}%")
    else:
        print(f"Sun: {result*100:.2f}%")

    
    

