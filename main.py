import sys
import time
from package.rocket import *
from package.user import*
from package.planningAndScheduling import *
from package.login import *

username = ''
while True:
    print("You want to login as:\n1. Admin\n2. User\n3. Exit\n")
    choice=int(onlyDigit(input("Enter your choice: ")))
    if choice == 1:
        print("Logging in as admin...")
        reply = adminLogin()
        if reply == True:
            print("Hello, welcome admin\nLogin Date and Time :",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"\n")
            adminMenu()
        else:
            print("Can't login as admin\n")

    elif choice == 2:
        print("Loging in as user...")

        while True:

            print("You want to:\n1. Login\n2. Sign Up\n3. Exit\n")
            choice = int(onlyDigit(input("Enter your choice: ")))

            if choice == 1:
                username = userLogin()
                if username == None:
                    print("Login failed!!!\n")
                    break
                print("Hello, welcome ",username,"\nLogin Date and Time :",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "\n")
                userMenu(username)
                # TODO remove remark
                printRemark(username)
            elif choice == 2:
                username = userSignup()
                if username == None:
                    print("Login failed!!!\n")
                    break
                print("Hello, welcome ",username,"\nCurrent Date and Time :",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "\n")
                userMenu(username)
                #TODO remove remark
                printRemark(username)
            elif choice == 2:
                break
            else:
                print("Invalid choice entered")

    elif choice == 3:
        print("Exiting...\nTHANK YOU FOR COMING!!!\nProgram Successfully Closed :)")
        break
    else:
        print("Invalid choice entered")



