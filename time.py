import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
print(type(hour))
if (hour>0 and hour<12):
    print("shubh prabhat")
elif (hour>=12 and hour<=17):
    print("shubh bapor")
else:
    print("shubh ratri")
    
