high = int(input("Enter high of triangle : "))

star = "*"
for i in range(high, 0, -1):
    print((i*' ' + star*(high-i) + star+(high-i)*star))
