

def sorted(numList=[]):
    min = 0
    max = 0
    for i in range(0, 10):
        for x in range(0, 10):
            if(numList[i] < numList[x]):
                continue
            elif (numList[i] > numList[x]):
                max = numList[i]
                min = numList[x]
                numList[i] = min
                numList[x] = max
            # print(numList)
    return numList


numArray = []
print("please enter 10 numbers")
for i in range(0, 10):
    input_num = int(input("number [" + str(i)+"]: "))
    numArray.append(input_num)

print("Array = ", numArray)
print("Sorted Array by descending = ", sorted(numArray))
