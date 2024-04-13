f=open("read.txt","r")
while True:
    text=f.readline()
    print(text)
    if not text:
        break