with open("sample.txt","w") as f:
    f.write("HAR HAR MAHADEV")
    f.truncate(3)
with open("sample.txt","r") as f:
    print(f.read())