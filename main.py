'''
COS 121
Homework #6
By Tristin Friend
Professor Troy Shotter
10/21/2024
'''

#countEvens
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
def countLarger(nums):
    result = []
    n = len(nums)

    for i in range(n):
        count = 0 
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                count +=1
        result.append(count)
    return result

nums = [5, 2, 6, 1]
print(countLarger(nums))

print ("------")

#isPalindrome
def isPalindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(12321))
print(isPalindrome(123))

print("------")

#fibGenerator
def fibGenerator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a +b

fib = fibGenerator()
fib_numbers = []

while len(fib_numbers) < 11:
    num = next(fib)
    if num > 10:
        fib_numbers.append(num)

print(fib_numbers)

print("------")

# Main
def main(): 
    print(countEven([2,3,4]))
    print(countLarger([5,2,6,1]))
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(12321))
    print(isPalindrome(123))
    print(fibGenerator(11))