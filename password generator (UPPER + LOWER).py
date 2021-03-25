#password will be generated with both upper and lowercase letters/symbols


#import modules
from random import randint


password = ""
for i in range(5):
    i = chr(randint(65,98))
    for x in range(5):
        x = chr(randint(65.98)).lower()
    password = str(password) + i + x


print(password)

#instead of giving the entire password length "10 characters", we split the uppercase and lowercase section evenly by a range of 5