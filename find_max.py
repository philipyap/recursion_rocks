# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

# def find_max(arr, largest=0, i=0):
#     if len(arr) == 1:
#         return arr[0]
#     elif largest == '':
#         largest = int(arr[i])
#     elif len(arr) < i + 1:
#         return largest
#     elif arr[i] >= largest:
#         largest = arr[i]
#         i += 1
#         return find_max(arr, largest, i)
#     else:
#         i += 1
#         return find_max(arr, largest, i)
#     # Write code here
    
def find_max(l):
    #base case
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], find_max(l[1:]))



print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45

# 1 vs find_max(l[1:])
        # 4 vs find_max(l[1:])
                # 45 vs find_max(l[1:])
                        # 6 vs find_max(l[1:])
                                # -50 vs find_max(l[1:])
                                        # 10 vs find_max(l[1:])
                                                # 2