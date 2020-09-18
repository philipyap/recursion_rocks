# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(string):
    # Write code here

    # base case
    if len(string) == 0:
        return ""
    # recursive step
    return string[-1] + string[:-1] # retu + reverse("comp")
    

# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
print(reverse("ab")) 
# => "ba"
print(reverse("computer")) 
# => "retupmoc"
print(reverse(reverse("computer"))) 
# => "computer"