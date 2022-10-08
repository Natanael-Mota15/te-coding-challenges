#                      Term 0 Review 
# Practice your knowledge of basic computer science concepts
# that we will continue to use in Term 1.
#
#

import numbers


print("-------- Challenge 1 --------")
# Challenge 1: Variables
# Prompt: Instantiate a variable and print its
# contents to the terminal.
#
greeting = ("Hello")
print(greeting)
print("-------- Challenge 2 --------")
# Challenge 2: Loops
# Prompt: Write a loop to print all of the odd
# integers in the given nums[] list but none of the even
# integers in the list.
#

nums = [1, 2, 4, 8, 11, 15, 16, 17, 18, 19, 21, 44, 49]
for i in nums:
    if (i % 2 != 0):
       print(i)
print("-------- Challenge 3 --------")
# Challenge 3: Function Definitions
# Prompt:  Write a function, array_sum, that calculates
# and prints the sum of the entries in a specified array.
# For example, calling array_sum on the array [1,3,2,7,3]
# should print 16 to the terminal.
#  array_sum([1, 3, 2, 7, 3]) --> 16
#  array_sum(nums) --> 225

def array_sum():
    listnum = []
    
    inputnum = input("what numbers you want to add")
    if (inputnum != "done"):
        inputnum = input("what numbers you want to add")
        listnum.append(int(inputnum))
    elif inputnum == "done":
        for numbe in range(0, len(listnum)):
            total =  total + listnum[numbe]
 


print("-------- Challenge 4 --------")
# Challenge 4: Function Calling
# Prompt: Call the function defined in challenge 3 on an array.
# of 5 or more numbers. Make sure it works
#
array_sum()

print("-------- Challenge 5 --------")
# Challenge 5:
# Prompt: Instantiate one variable that will store a string, name.
# Instantiate another variable that will store a number, age.
# Print the following string by accessing your two variables:
# 'I am _name_ and I am _age_ years old'
#
name = "Natanael"
age = "15"

print(f"I am {name} and I am {age} years old.")
print("-------- Challenge 6 --------")
# Challenge 6:
# Prompt: Write a Python function, compute_area, that will accept
# the base and height of a triangle as parameters and return
# the computed area. 
# For example, calling compute_area with the arguments 3 (height) and 
# 4 (base), the function should return 6:
# compute_area(3, 4) --> 6
#
#
base = input("what is the base")
height = input("What is the height")
base1 = int(base)
height2 = int(height)
answer = (base1 * height2)/2
print(answer)
print("-------- Challenge 7 --------")
# Challenge 7:
# Prompt: Write a Python function, max_min, that will accept
# a list of integers as a parameter and print the largest
# and smallest integers.
# max_min(nums) --> 1    49
# max_min([1, 3, 2, 7, 3]) --> 1, 7 
#

numlist = []
nu = input("What numbers you want to sort, type done when done")
if nu == "done":
    numlist.sort()
    print(numlist[0])
    numb = len(numlist)
    print(numlist[numb])
else:
    nu = input("What numbers you want to sort, type done when done")
