import random
passlen = int(input("enter the length of the password"))
s = "abcdefghijklmnopqrstuvwxyz01234567890.ABCDEFGHIJKLMNOPQRSTUVWXYZ1@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print(p)