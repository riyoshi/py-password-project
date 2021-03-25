#import modules
from random import randint


#password will be generated in all uppercase letters (along with other symbols)
password = ""
for i in range(10):
    i = chr(randint(65, 98))
    password = str(password) + i
print(password)




