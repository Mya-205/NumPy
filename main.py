import numpy as np

##
# Arrays and using the index number
##
arr = np.array([9, 4, 7, 2, 6, 8, 4, 8])
print(arr)
index = input("Please choose the index number: ")
index = int(index)
print(arr[index])

##
# Printing a list of random numbers
##

nums = []
amount = 10
Numbers = np.random.randint(0, 10, 10)
print(Numbers)

##
# Finds the minimum and maximum value of these numbers, and the sum of all of the numbers
##
min = min(Numbers)
max = max(Numbers)
sums = sum(Numbers)
print(f"The minimum value is {min}")
print(f"The maximum value is {max}")
print(f"The sum of all these numbers is {sums}")


##
#Prints the NumPy version
##

print(f"The version of this NumPy is {np.__version__}")
