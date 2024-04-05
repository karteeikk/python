import time
x=time.strftime('%H:%M:%S')
print(x)
'''print(time.strftime('%H'))
print(time.strftime('%M'))
print(time.strftime('%S'))'''
if int(time.strftime('%H'))<=12:
        print("good morning")
elif int(time.strftime('%H'))>=12 and int(time.strftime('%H'))<=17:
    print("good afternoon")
else:
      print("good evening")
