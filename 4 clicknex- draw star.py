high = int(input("Enter high of triangle : "))

star = "*"
for i in range(0, high+1, 1):
    if(i == 0):
        continue
    print((i)*' ' + (high-i)*star + star+(high-i)*star)
