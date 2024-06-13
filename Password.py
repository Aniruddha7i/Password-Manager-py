

def view(yourId):
    file = open("password.txt","r")
    users=file.readlines()
    for user in users:
        (userId,password) = user.split(":")
        if(yourId==userId.lower()):
            print(f"View Mode: {userId} : {password}")
            return True
    return False

    
def add():
    file = open("password.txt","a")
    file.write("\nThis will add this line77")


def main():
    print("This is a Password Manager System")
    while(True):
        mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit?").lower()
        if(mode=="q"): 
            break
        elif(mode=="view"):
            userId=input("Enter your user name: ").lower()
            if(view(userId)==False):
               print(f"Error: This {userId} user name is not present")
        elif(mode=="add"):
            add()
        else:
            print("Invalid mode.")
    
    print("Think You for using our system")
    

if __name__ == '__main__':
    main()