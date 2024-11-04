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

print ("------")

#isPalindrome
def is_palindrome(s): 
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man, a plan, a canal, Panama"))

print("------")

def fibGenerator(size):
    if size < 2:
        return []
    
    fib_sequence = [0,1]

    while len(fib_sequence) < size:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

print(fibGenerator(10))
print(fibGenerator(12))

print("------")