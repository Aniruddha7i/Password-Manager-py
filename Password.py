import maskpass  # importing maskpass library
import base64

def view(yourId):
    print("\n")
    file = open("password.txt","r")
    users=file.readlines()
    for user in users:
        (name,userId,password) = user.split(" : ")
        if(yourId==userId.lower()):
            # Decoding the string
            decodePassword = base64.b64decode(password[1:]).decode("utf-8")
             
            print(f"View Mode:\n Name: {name}\n userName: {userId}\n Password: {decodePassword}")
            print("\n")
            return True
    return False

    
def add():
    userName = input("Enter your username: ")
    name = input("Enter your name: ")
    print("Enter your password (mininum length of your password is 4): ")
    password = maskpass.askpass(prompt="Password:", mask="#")
    
    if(len(password)<4):
        print("Error: password is not secure, Password must heve mininum length of 7")
        add()
    else:
        # Encoding the string
        encodePassword = base64.b64encode(password.encode("utf-8"))
        
        file = open("password.txt","a")
        file.write(f"{name} : {userName} : {encodePassword}\n")

def edit():
    pass

def main():
    print("This is a Password Manager System")
    while(True):
        mode = input("Would you like to add a new password or view existing ones (view, add, edit), press q to quit? ").lower()
        if(mode=="q"): 
            break
        elif(mode=="view"):
            userId=input("Enter your user name: ").lower()
            if(view(userId)==False):
               print(f"Error: This {userId} user name is not present")
        elif(mode=="add"):
            add()
            print("Add Successfully!!")
        elif(mode="edit"):
            edit()
            print("Edit Successfully!!")
        else:
            print("Invalid mode.")
    
    print("Think You for using our system")
    

if __name__ == '__main__':
    main()