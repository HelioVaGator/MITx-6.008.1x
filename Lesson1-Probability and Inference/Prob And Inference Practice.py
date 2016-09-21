# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:24:57 2016

@author: harshavarg
"""

import comp_prob_inference

n = 100000
heads_so_far = 0
fraction_of_heads = []
for i in range(n):
    if comp_prob_inference.flip_fair_coin() == 'heads':
        heads_so_far += 1
    fraction_of_heads.append(heads_so_far / (i+1))


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 4))
plt.plot(range(1, n+1), fraction_of_heads)
plt.xlabel('Number of flips')
plt.ylabel('Fraction of heads')


model = {'heads': 1/2, 'tails': 1/2}
sample_space = set(model.keys())

model['heads']
model['tails']

model = {}
for i in range(1, 6+1):
    for j in range(1, 6+1):
        model[(i, j)] = 1/36
        
        
def prob_of_event(event, prob_space):
    total = 0
    for outcome in event:
        total += prob_space[outcome]
    return total
    
    
prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
rainy_or_snowy_event = {'rainy', 'snowy'}
print("prob:")
print(prob_of_event(rainy_or_snowy_event, prob_space))




random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
W = random_outcome
if random_outcome == 'sunny':
     I = 1
else:
     I = 0
    
print (I)

W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}
I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}

random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
W = W_mapping[random_outcome]
I = I_mapping[random_outcome]

W_table = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
I_table = {0: 1/2, 1: 1/2}


W = comp_prob_inference.sample_from_finite_probability_space(W_table)
I = comp_prob_inference.sample_from_finite_probability_space(I_table)


