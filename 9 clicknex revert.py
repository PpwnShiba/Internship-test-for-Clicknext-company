
input_word = str(input("Enter sentence or word : "))
numofchar = len(input_word)
print(numofchar)

revertedArray = []

for i in range(0, numofchar):
    revertedArray.append(input_word[numofchar-1-i])

for i in range(0, len(revertedArray)):
    print(revertedArray[i], end="")
