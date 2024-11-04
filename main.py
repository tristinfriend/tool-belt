'''
COS 121
Homework #6
By Tristin Friend
Professor Troy Shotter
10/21/2024
'''

# countEvens
def countEven (alist):
    c = 0
    for i in alist:
        if i % 2 == 0:
            c += 1
    return c 

x = countEven([2,3,4])
print(x)

print("------")

# countLarger
def countLarger(numArray, x):
    return sum(1 for num in numArray if num > x)

numArray = [8, 12, 40, 10]
numLarger = countLarger(numArray, 10)
print(numLarger) 
