
def findChange(price):
    change = 1000-price
    print('Change : '+str(change)+' Baht')
    if(change // 500 != 0):
        print('500 Baht '+str(change//500)+' bank bill')
        change = change-500
    if(change // 100 != 0):
        print('100 Baht '+str(change//100)+' bank bill')
        change = change - (change//100)*100
    if(change // 50 != 0):
        print('50 Baht '+str(change//50)+' bank bill')
        change = change - (change//50)*50
    if(change // 10 != 0):
        print('10 Baht '+str(change//10)+' coin')
        change = change - (change//10)*10
    if(change // 5 != 0):
        print('5 Baht '+str(change//5)+' coin')
        change = change - (change//5)*5
    if(change // 1 != 0):
        print('1 Baht '+str(change//1)+' coin')


price = int(input("Enter price : "))

while(price >= 1000):
    print("Please input price less than 1000.")
    price = int(input("Enter price : "))

findChange(price)
