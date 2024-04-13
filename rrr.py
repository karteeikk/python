import random   
import string  
import secrets 
num=10   
res=''.join(secrets.choice(string.ascii_letters+string.digits) for x in range(num))  
  
print("Secure random string is :"+str(res))  