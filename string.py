print('mahadev')    #single quoation
print("mahadev")    #double quoation

a="mahadev" #assign string to the variable
print(a)

b="""sutex bank college of computer application and science"""    #multiline strings
print(b)

#string are charactor array
print(a[1])
print(a[4])

for x in "banana":
    print('jovo : ',x)


#python slicing strings
c="hello, world!"     #start index alwayss 0
print(c[2:5])
print(c[:5])    #slice from the start
print(c[2:])    #slice to the end
print(c[-5:-2])     #negative indexing

txt='bharatmata'
dfg=('sdfsf','fsdfs','dsfsdf')
temp="jay javan jay kisan"
m=txt.center(40)
n=txt.count(txt)
o="#".join(dfg)
p=len(txt)
q=max(txt)
r=min(txt)
s=temp.replace("jay","amar",1)
t=txt.lower()
u=txt.upper()
v=temp.split()
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)

x="    !!!!hello woels!!!!!"
print(x.strip())   #remove space start or end
print(x.rstrip("!"))  #end sign remove
print(x.endswith("!"))
print(x.endswith("l",3,6))

block="introduction kartik's world"
print(block.capitalize())

name="agdshAFDJ425"
jas="fsdSAS"
print(name.isalnum())
print(jas.isalpha())
print(name.isprintable())
print(name.isspace())

title="World Health Organization"
print(title.istitle())

temo="python very easy"
print(temo.startswith("python"))
print(temo.swapcase())

suraj="the legend of india"
print(suraj.title())