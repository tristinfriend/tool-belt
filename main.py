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
def is_palindrome(s): 
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man, a plan, a canal, Panama"))

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