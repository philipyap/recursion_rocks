# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
import random

def coin_flips(n, result=[]):
    
    str1=""
    for i in range(n):
        flip = random.choice(['H', 'T'])
        str1 = str1 + flip
    if (len(result)< 1):
        result.append(str1)

    elif (len(result)==2**n):
        return result

    else: 
        for item in result: 
            pass
        else:
            result.append(str1)

    return coin_flips(n, result)        
    # Write code here
    # pass
print(coin_flips(3))
# print(coinFlips(2)) 
# => ["HH", "HT", "TH", "TT"]