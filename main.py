'''
COS 121
Homework #6
By Tristin Friend
Professor Troy Shotter
10/21/2024
'''

# countEvens
def countEvens (aArray):
    Ec = 0
    for i in aArray:
        if i % 2 == 0:
            Ec += 1
    return Ec

# countLarger
def countLarger(numArray, x):
    cL = 0
    for i in (numArray):
        if i > x:
            cL += 1
    return cL


# isPalindrome
def isPalindrome(aString):
    aString = aString.lower()
    stringSize = len(aString)
    for i in range (stringSize):
        x = (aString[stringSize-i-1])
        y = (aString [i])
        if x != y:
            return False
    return True

# fibGenerator
def fibGenerator(size):
    fib_numbers = [0,1]
    a, b = 0, 1  
    if size < 2:
        return []
    while len(fib_numbers) < size:
        c = a + b
        fib_numbers.append(c)
        a=b
        b=c 

    return fib_numbers

# Main
def main():
    print(countEvens([4,6,1,3,9,10]))
    print(countEvens([4,6,100,0,9,10]))
    print(countLarger([1,100,80,20],20))
    print(countLarger([1,5,4,80,20],20))
    print(isPalindrome("Racecar"))
    print(isPalindrome("HelloWorld"))
    print(fibGenerator(1))
    print(fibGenerator(10))
    print(fibGenerator(15))

main()