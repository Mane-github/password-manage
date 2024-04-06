#password manager
#website/email (mahendramane1920@gmail.com)
#password 192021


import os
import random
from cryptography.fernet import Fernet
import questionary

print("welcome to password manager!")

if not (os.path.exists("key.key")):
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
        
if not (os.path.exists("password.txt")):
    with open("password.txt", "w") as file:
        pass        

if os.path.exists("pin.txt"):
    with open("pin.txt", "r") as file:
        code=file.read()
        
    user_code = input("\nEnter the code: ")
    
    if user_code == code:
        print()
        
        user_input=questionary.select("choose any one of the following:",choices=["add a password","view stored password"]).ask()
        
        if user_input == "add a password":
            #adding password to the file
            website=input("\nEnter the website name/email: ")
            password=questionary.password("enter the password to stored: ").ask()
            
       # encrypt the password and store it in the file
            with open("key.key", "rb") as file:
                key=file.read()
                cipher=Fernet(key)
            encrypted_password=cipher.encrypt(password.encode()).decode()    
            with open("password.txt", "a") as file:
                file.write(f"{website}||{encrypted_password}\n")
            print("password added succesfully!")    
         
              
            
        else:
            # viewing stored password
            with open("password.txt", "r") as file:
                file_lines=file.readlines()
                
                
                for index, line in enumerate(file_lines):
                    line=line.strip()
                    user_website,user_password=line.split("||")
                    with open("key.key", "rb") as file:
                        key=file.read()
                        cipher=Fernet(key)
                        decrypted_password=cipher.decrypt(user_password.encode()).decode()
                        print(f"\n{index+1})website/email: {user_website}\npassword:{decrypted_password}")
                    print() 
                
                  
    else:
        print("Incorrect code!")
        
    
else:
    code=str(random.randint(1000, 2000))
    with open("pin.txt", "w") as file:
        file.write(code)
        
    print(f"\nYour code to enter the application is{code}")
    print("You will be shown this code only once.")
    
    user_code = input("\nEnter the code: ")
    
    
if user_code == code:
        print()
        
        user_input=questionary.select("choose any one of the following:",choices=["add a password","view stored password"]).ask()
        
        if user_input == "add a password":
            #adding password to the file
            website=input("\nEnter the website name/email: ")
            password=questionary.password("enter the password to stored: ").ask()
            
       # encrypt the password and store it in the file
            with open("key.key", "rb") as file:
                key=file.read()
                cipher=Fernet(key)
            encrypted_password=cipher.encrypt(password.encode()).decode()    
            with open("password.txt", "a") as file:
                file.write(f"{website}||{encrypted_password}\n")
            print("password added succesfully!")    
         
              
            
        else:
            # viewing stored password
            with open("password.txt", "r") as file:
                file_lines=file.readlines()
                if file_lines:
                 for index, line in enumerate (file_lines):
                    line=line.strip()
                    user_website,user_password=line.split("||")
                    with open("key.key", "rb") as file:
                        key=file.read()
                        cipher=Fernet(key)
                        decrypted_password=cipher.decrypt(user_password.encode()).decode()
                        print(f"\n{index+1})website/email: {user_website}\npassword:{decrypted_password}")
                    print() 
                    
                 
                      
else:
        print("Incorrect code!")
        