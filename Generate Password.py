import random

# Taking input from user
passlen = int(input("Enter the length of password"))

# Stored letters(Upper and Lower Case), Numbers and Special Characters in s variable
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# random sampling by joining the length of password
p = "".join(random.sample(s,passlen ))
print(p)