
def compared(str1, str2):

    lenStr1 = len(str1)
    lenStr2 = len(str2)

    str1Array = []
    str2Array = []

    numOfTrue = 0

    if(lenStr1 == lenStr2):
        for i in range(0, lenStr1):
            if(str1[i] not in str1Array):
                str1Array.append(str1[i])
                lenStr1 = len(str1Array)
                # print(str1Array)
            if(str2[i] not in str2Array):
                str2Array.append(str2[i])
                lenStr2 = len(str2Array)
                # print(str2Array)

        # for i in range(0, lenStr1-1):
        #     if(str1[i] == str1[i+1]):
        #         print(str1[i], str1[i+1])
        #         str1Array.pop(i)
        #         lenStr1 = len(str1Array)
        #     if(str2[i] == str2[i+1]):
        #         print(str2[i], str2[i+1])
        #         str2Array.pop(i)
        #         lenStr2 = len(str2Array)

        for i in range(0, lenStr1):
            for x in range(0, lenStr2):
                if(str1Array[i] == str1Array[x]):
                    numOfTrue = numOfTrue+1
            # numOfCharRedun =

        if(numOfTrue == lenStr1):
            return print('True')
        else:
            return print('False')
    else:
        return print('False')


string1 = str(input("Enter string 1 : "))
string2 = str(input("Enter string 2 : "))

compared(string1.lower(), string2.lower())
