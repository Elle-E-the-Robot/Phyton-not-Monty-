import random


usable = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Parola uzunluğunu giriniz: "))
password = ""

for i in range(length):
    ae = random.choice(usable)
    password += ae
print(password)
