

aString = "Hello"

# Reading characters
for i in range(len(aString)):
    print(aString[len(aString)-1-i])

aList = [9,2,7,5]
listSize = len(aList)
for i in range(listSize):

    print(aList[listSize-i-1])

for i in range(len(aList)):
    print(aList[-i])


def countTwos(aList)
    counter = 0
    for i in aList: 
        if i == 2:
                counter += 1
    #print("------"
    #print(counter)
    return counter #sebds information back to the call


print("------")
print(counter)

x = countTwos([2,5,2,10])
print(x)
countTwos([10,5,20])