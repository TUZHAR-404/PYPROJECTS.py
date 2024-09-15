import random

password = 'ASDFGHJKLZXCVBNMQWERTYUIOPasdfghjklqwertyuiopzxcvbnm1234567890!@#$%^&*()'
len = int(input("enter lenght of your password:"))

a = (random.sample(password,len))

print(f"This is your new password:{a}")

