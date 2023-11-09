import random

response = input("How strong of a password do you need? 1 = weak 2 = strong. ")
weakpass = ["12345","Password","password123","123","password"]
lestpass = ["9", "30", "21", "17", "12", "22", "15"]
alp = [qwertyuiopasdfghjklzxcvbnm]

if response == "1":
    var1 = "weak"
    password = random.choice(weakpass)
elif response == "2":
    var1 = "strong"
    lenpass = int(random.choice(lestpass))

else:
    print("Not a acceptable response.")
print("Your " + var1 + " password is: " + password + ".")