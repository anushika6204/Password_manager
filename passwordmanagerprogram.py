#CONCEPTS USE
#1 - DISCTIONARY
#2 - LOOPS
#3 - CONDITIONAL
#4 - MPDULE: RANDOM
#5 - FILE HANDLING - file read/write


import random
import string

passwords = {}

#load existing password file
try:
    with open("password.txt", "r") as file:
       for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    passwords = "".join(random.choice(chars) for _ in range(8))
    return passwords

while True:
     print("\n----PERSONAL PASSWORD MANAGER----")
     print("1. Save Password")
     print("2. view Passwords")
     print("3. Generate Password")
     print("4. Exit")

     choice = input("enter your choice: ")

     if choice == "1":
         site = input("enter website: ")
         pwd = input("enter password: ")

         passwords[site] = pwd


         with open("password.txt",  "a") as file:
             file.write(f"{site}:{pwd}\n")

         print("saved!")

     elif choice == "2":
         if not passwords:
             print("No data")
         else:
             for site, pwd in passwords.items():
                 print(site, ":", pwd) 

     elif choice == "3":
         print("Generated Password", generate_password())

     elif choice == "4":
         print("ok bye...")
         break
     else:
         print("In-valid input")


         

