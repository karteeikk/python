'''f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()

'r'=read file
'a'=append file
'w'=writr file
'''
with open("myfile.txt") as f:
    text=f.read()
    print(text)