
timeSecond = int(input("Enter Time Second : "))

hour = timeSecond//3600
minute = (timeSecond % 3600)//60
second = (timeSecond % 3600) % 60

if(timeSecond <= 59):
    print('Your time : 00:00:'+str(second))
elif(timeSecond >= 60):
    if(second < 10):
        print('Your time : 00:' + str(minute) + ":" + str(second))
    elif(hour == 0 and minute < 10):
        print('Your time : 00:' + str(minute) + ":" + str(second))
    elif(hour == 0 and minute >= 10):
        print('Your time : 00:' + str(minute) + ":" + str(second))
    elif(hour >= 1):
        print('Your time : '+str(hour)+':' + str(minute) + ":" + str(second))
