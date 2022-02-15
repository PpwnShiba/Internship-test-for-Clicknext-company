#1 Finds the sum of matching numbers in an array.
listElement = []

numOfElement = int(input("Enter number of elements : "))

for i in range(0,numOfElement):
    inputelement = int(input("Enter element : "))
    listElement.append(inputelement) #add to list

print("Array = ",listElement)

sum = int(input("Enter sum : "))
check = 0

for i in range(0, numOfElement):
    num = len(listElement)
    for z in range(0, num):
        if(i == z):
            continue
        if(listElement[i] + listElement[z] == sum):
            check = 1
            # print("I Z : ",i,z)
            # print(listElement)
            print("Result is ",listElement[i], listElement[z])
            listElement.pop(z)
            if(i == 0 ):
                listElement.pop(i)
            else:
                listElement.pop(i-1)
            # print(listElement)
            # print(len(listElement))
            break
          
if(check == 0):
    print("can't find element because the sum you want is higher than sum of max and min in array")

