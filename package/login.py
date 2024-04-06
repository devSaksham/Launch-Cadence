import sys
from package.rocket import *
from package.user import*
from package.planningAndScheduling import *

adminUsername="sakshamAgrawal"
adminPassword="qwerty@13"

def adminLogin(count=1):
    if count >= 4:
        print("You  are out of attempts!!!")
        return False
    admin_username=input("\nEnter admin username: ")
    admin_password=input("Enter admin password: ")

    if admin_username == adminUsername and admin_password == adminPassword:
        print("Login successfully!!! ")
        return True
    else:
        print("Enter correct username and password!!")
        print("Only {} attempts left!!!".format(3-count))
        adminLogin(count+1)

def userSignup():
    addUser()
    print("Redirecting to login...")
    print("Kindly Login.")
    return userLogin()

def userLogin():
    count = 1
    user=getUser()
    username = input("Enter username: ")

    if username not in user:

        choice = input("Username does not exist do you want to sign up?(yes/no): ").lower()

        if choice == "yes":
            print("Redirecting to sign up...\n")

            return userSignup()
        else :
            return
    else:
        while True:
            if count >=4:
                print("You are out of attempts!!!")
                return

            password = input("Enter password: ")

            if user[username] == password:
                print("Logged in successfully\n")
                return username
            else:
                print("Enter correct password.")
                print("Only {} attempts left !!!\n".format(3 - count))
                count += 1

def userMenu(username):
    updateLaunchCompletion()
    updateLaunchCompletion(username)
    while True:
        print("Main Menu:\n1.  View Profile\n2.  Update Profile\n3.  View Launch Vehicles\n4.  View Launch Vehicle Prices\n5.  View Slots\n6.  Search Slots\n7.  Book Slot\n8.  Cancel Booking\n9.  Active Booking\n10. Booking History\n11. Delete Profile\n12. View Remarks\n13. Exit\n")
        choice = input("Enter your choice (1-13): ")

        match choice:
            case "1":
                print("Viewing Profile for", username,'\n')
                displayProfile(username)
            case "2":
                print("Updating Profile for", username,'\n')
                updateProfile(username)
            case "3":
                print("Viewing Launch Vehicles for", username,'\n')
                displaySpecs()
            case "4":
                print("Viewing Launch Vehicle Prices for", username,'\n')
                displayPrice()
            case "5":
                print("Viewing Slots for", username,'\n')
                printSlots()
            case "6":
                print("Searching Slots for", username,'\n')
                search()
            case "7":
                print("Booking Slot for", username,'\n')
                bookSlot(username1=username)
            case "8":
                print("Canceling Booking for", username,'\n')
                cancelBooking(username)
            case "9":
                print("Displaying Booking for", username, '\n')
                slots = readSlot(username+'_active_booking.txt')
                if slots != None :
                    printSlots(slots)
                else:
                    print("No bookings available.\n")
            case "10":
                print("Booking History for", username, '\n')
                displayBookingsHistory(username)
            case "11":
                print("Deleting Profile for", username,'\n')
                deleteUser(username)
            case "12":
                print("printing remarks...")
                printRemark(username)
            case "13":
                while True:
                    answer = input("Enter 1 to exit program or Enter 2 to exit menu: ")
                    if answer == "1":
                        print("Exiting...\nTHANK YOU FOR COMING!!!\nProgram Successfully Closed :)")
                        sys.exit()
                    elif answer == '2':
                        print("\nExiting the menu...\n")
                        return  # Exit the menu
                    else:
                        print("Invalid choice entered")

            case _:
                print("Invalid choice! Please enter a number between 1 and 13.\n")
def adminMenu():
    updateLaunchCompletion()
    while True:
        print("Main Menu:\n1.  View Launch Vehicle\n2.  View Launch Price\n3.  Add Launch Vehicle\n4.  Update Price\n5.  Update Config. of Launch Vehicle\n6.  Delete Launch Vehicle\n7.  View Slots\n8.  Search Slot\n9.  Update Slot\n10. Update Slot Status\n11. Display Booking History\n12. Add Slot\n13. Delete Slot\n14. Exit\n\n")

        choice = input("Enter your choice (1-14): ")
        if choice == "1":
            print("\nViewing Launch Vehicle...")
            displaySpecs()
        elif choice == "2":
            print("\nViewing Launch Vehicle Price...")
            displayPrice()
        elif choice == "3":
            print("\nAdding Launch Vehicle...")
            addRocket()
        elif choice == "4":
            print("\nUpdating Price...")
            updatePrice()
        elif choice == "5":
            print("\nUpdating Config. of Launch Vehicle...")
            updateSpecs()
        elif choice == "6":
            print("\nDeleting Launch Vehicle...")
            deleteRocket()
        elif choice == "7":
            print("\nViewing Slots...")
            printSlots()
        elif choice == "8":
            print("\nSearching Slot...")
            search()
        elif choice == "9":
            print("\nUpdating Slot...")
            updateSlot()
        elif choice == "10":
            print("\nUpdating Slot Status...")
            updateSlotStatus()
        elif choice == "11":
            print("\nDisplaying Booking History...")
            displayBookingsHistory()
        elif choice == "12":
            print("\nAdding Slot...")
            addSlot()
        elif choice == "13":
            print("\nDeleting Slot...")
            deleteSlot()
        elif choice == "14":
            while True:
                answer = input("Enter 1 to exit program or Enter 2 to exit menu: ")
                if answer == "1":
                    print("\nExiting...\nTHANK YOU FOR COMING!!!\nProgram Successfully Closed :)")
                    sys.exit()
                elif answer == '2':
                    print("\nExiting the menu...\n")
                    return  # Exit the menu
                else:
                    print("Invalid choice entered")

        else:
            print("Invalid choice! Please enter a number between 1 and 14.\n")

