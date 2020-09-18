# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):

    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)
factorial(5)
# print(factorial(5))
# => 120