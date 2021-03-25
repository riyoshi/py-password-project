#password will be generated in all lowercase letters

#import modules
from random import randint


password = ""
for i in range(5):
    i = chr(randint(65,98)).lower()
for x in range(5):
    x = chr(randint(65,98)).lower()

    password = str(password) + i + x




print(password)