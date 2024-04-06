import time
import sys
from datetime import datetime
from package.rocket import *
from package.user import*

# Function to check if a year is a leap year
def isLeap(year): #working
    if (year%4==0 and year%100!=0 )or year%400==0:
        return True
    else:
        return False

# Function to input a valid date from the user
def inputDate():#working
    month=''
    day=''
    year=''
    while True:
        year=onlyDigit(input("Enter the year:"))
        if int(year)>2023 and int(year)<10000:
            break
        else:
            print("Enter the year between 2024 to 9999")

    while True:
        month=onlyDigit(input("Enter month:"))
        if int(month) in [i for i in range(1,13)]:
            break
        else:
            print("Enter integer between 1 to 12!!!")
    while True:
        day=onlyDigit(input("Enter the day:"))
        if int(month)==2:
            if isLeap(int(year)):
                if int(day) in [i for i in range(1,30)]:
                    break
                else:
                    print("Enter integer between 1 to 29!!!")
            else:
                if int(day) in [i for i in range(1,29)]:
                    break
                else:
                    print("Enter integer between 1 to 28!!!")
        elif int(month) in {1,3,5,7,8,10,12}:
            if int(day) in [i for i in range(1,32)]:
                break
            else:
                print("Enter integer between 1 to 31!!!")
        else:
            if int(day) in [i for i in range(1,31)]:
                break
            else:
                print("Enter integer between 1 to 30!!!")
    date=year+"-"+month+"-"+day
    return date

# Function to append a slot to the launch_slot.txt file
def appendSlotFile(slot):#working
    s=''
    with open ("launch_slot.txt","a") as fp:
        for i in slot:
            s+=i+"~"+slot[i]+"|"
        s+="\n"
        fp.write(s)

# Function to write slots to the launch_slot.txt file
def dynamicPrice(slots):
    currentDate = datetime.today()
    for slot in slots:
        if (datetime.strptime(slot["DATE"], "%Y-%m-%d" ) - currentDate).days < 30:
            slot["PRICE"] = str(int(slot["PRICE"]) +int(slot["PRICE"])*.15)
    return slots

def writeSlotFile(slots):
    with open ("launch_slot.txt","w") as fp:
        #slots is a list here
       s=''
       for slot in slots:
           for i in slot:
               s+=i+"~"+slot[i]+"|"
           s+="\n"
       fp.write(s)

# Function to read slots from a file
def readSlot(filename = None):
    l=[]
    try:
        if filename == None:
            filename = "launch_slot.txt"
        with open(filename,"r") as fp:
            for line in fp.readlines():
                line=line.strip('\n')
                l2=line.split('|')
                l2.pop()
                slot={}
                for i in l2:
                    j=i.split("~")
                    slot.update({j[0]:j[1]})
                l+=[slot]
        return l
    except :
        print('',end='')

# Function to print slots information
def printSlots(slots = None):
    if slots==None:
        slots=readSlot()

    for i,j in enumerate(slots):
        print("{}-> DATE:{}\n    LAUNCH VEHICLE:{}\n    DESTINATION:{}\n    MAX PAYLOAD:{} kg\n    PRICE:${}k per kg\n    STATUS:{}\n    BOOKING STATUS:{}".format(i+1,j["DATE"],j["LAUNCH VEHICLE"],j["DESTINATION"],j["MAX PAYLOAD"],j["PRICE"],j["STATUS"],j["BOOKING STATUS"]))
        if len(j)==9:
            print("    TIME:{}\n    PAYLOAD:{}\n".format(j["TIME"],j["PAYLOAD"]))
        if len(j)==10:
            print("    USERNAME:",j["USERNAME"],"\n")
        print('')

# Function to add a new slot
def addSlot():
    slot={}
    specs = specsDict()
    price = priceDict()
    date = inputDate()

    rocket=""
    rName = [i for i in price]
    #printing a menu to choose rocket
    while True:
        print('')
        for i, j in enumerate(rName):
            print(i + 1, ".", j, sep="")

        choice = onlyDigit(input("\nChoose the Launch Vehicle from above: "))

        if int(choice) > 0 and int(choice) <= len(rName):
            rocket = rName[int(choice) - 1]
            print('')
            break
        else:
            print("Invalid choice entered\n")

    print("You chose {}.".format(rocket))
    # Getting necessary information from the user and add a new slot
    try:
        keyword=[i for i in specs[rocket]]
        for spec in specs[rocket]:
            print(spec+":"+specs[rocket][spec])
        orbit=''
        while True:
            orbit=input("choose the orbit from above:").upper()
            if orbit in specs[rocket].keys():
                break
        slot={
            "DATE":date,
            "LAUNCH VEHICLE":rocket,
            "DESTINATION":orbit,
            "MAX PAYLOAD":specs[rocket][orbit],
            "PRICE":price[rocket][orbit],
            "STATUS":"ACTIVE",
            "BOOKING STATUS":"AVAILABLE"
        }
        appendSlotFile(slot)
        print("\nNew slot successfully added!!!\n")
    except KeyError:
       print("\nOrbit Does Not Exist!!!\n")

# Function to update an existing slot
def updateSlot(slots = None):
    if slots == None:
        slots=readSlot()

    printSlots(slots)
    specs=specsDict()
    price=priceDict()
    while True:
            num=int(onlyDigit(input("Enter the number corresponding to the slot you want to edit (or enter 0 to exit): ")))
            if num==0:
                print("Exiting update mode!")
                return
            elif num < 1 or num > len(slots):
                print("Invalid slot number! Please enter a valid slot number.")
            else:
                break

    slotToEdit=slots[num - 1]
    print("Slot To Edit:-")
    printSlots([slotToEdit])

    while True:
        newRocket=input("Enter the new rocket name (leave blank to keep current rocket '{}'): ".format(slotToEdit["LAUNCH VEHICLE"])).upper()
        if newRocket=="":
            newRocket=slotToEdit["LAUNCH VEHICLE"]
            break
        elif newRocket in (specsDict()).keys():
            slotToEdit["LAUNCH VEHICLE"]=newRocket
            print("Rocket '{}' selected.\n".format(newRocket))
            break
        else:
            print("Invalid rocket name! Please choose from the available rockets.\n")
            for i in specs:
                print(i)

    displaySpecsOfParticularRocket(newRocket)

    while True:
        try:
            orbit=input("Choose the orbit from available options: ").upper()
            if orbit in specs[newRocket]:
                slotToEdit["DESTINATION"]=orbit
                slotToEdit["MAX PAYLOAD"]=specs[newRocket][orbit]
                slotToEdit["PRICE"]=price[newRocket][orbit]
                print("Rocket details updated successfully!")
                break
            else:
                print("Invalid orbit selected! :(")

        except KeyError:
            print("Invalid orbit selected! :(")

    # Update the slot file with the modified slot information
    slots[num - 1]=slotToEdit
    writeSlotFile(slots)
    print("Slot updated successfully :)")

# Function to search for slots based on various criteria
def search(slots = None):
    if slots == None:
        slots = readSlot()

    choice = None
    while True:
        print("Keyword Menu:-\n1. Rocket\n2. Destination\n3. Month of launch\n4. Booking Status\n5. Status\n6. Exit\n")
        choice = int(onlyDigit(input("Enter the number corresponding to the keyword to search for: ")))
        if choice == 1:
            print("\nYou selected: Rocket")
            printSlotsByRocket(slots=slots)
        elif choice == 2:
            print("\nYou selected: Destination")
            printByOrbit(slots=slots)
        elif choice == 3:
            print("\nYou selected: Month of launch")
            printSlotsByMonth(slots=slots)
        elif choice == 4:
            print("\nYou selected: Booking Status")
            printSlotByBookingStatus(slots=slots)
        elif choice == 5:
            print("\nYou selected: Status")
            printSlotByStatus(slots=slots)
        elif choice == 6:
            while True:
                answer = input("Enter 1 to exit program or Enter 2 to exit menu: ")
                if answer == "1":
                    print("\nExiting the program...\n")
                    sys.exit()
                elif answer == '2':
                    print("\nExiting the menu...\n")
                    return  # Exit the menu
                else:
                    print("Invalid choice entered")

        else:
            print("Invalid choice! Please select a number between 1 and 6.\n")

# Function to update the status of a slot
def updateSlotStatus():
    slots = readSlot()
    printSlots(slots)

    while True:
            slotNum = int(onlyDigit(input("Enter the number corresponding to the slot you want to update status for (or enter 0 to exit): ")))
            if slotNum == 0:
                print("Exiting update status mode!")
                return
            elif slotNum < 1 or slotNum > len(slots):
                print("Invalid slot number! Please enter a valid slot number.")
            else:
                break

    slotToEdit = slots[slotNum - 1]
    print("Current status for the slot:", slotToEdit["STATUS"])

    newStatus = input("Enter the new status for the slot (ACTIVE, INACTIVE): ").upper()
    if newStatus in ["ACTIVE", "INACTIVE"]:
        slotToEdit["STATUS"] = newStatus
        slots[slotNum - 1] = slotToEdit
        writeSlotFile(slots)
        print("\nSlot status updated successfully!\n")
    else:
        print("\nInvalid status entered! Status remains unchanged.\n")

# Function to update the booking status of a slot
def updateBookingStatus(slotToUpdate,currentStatus ):
    slots = readSlot()
    try:
        indexToUpdate=slots.index(slotToUpdate)
        slots[indexToUpdate]["BOOKING STATUS"] = currentStatus
        writeSlotFile(slots)
    except ValueError:
        print("Error updating slot in launch_slot.txt")
    except:
        print("Error updating slot in launch_slot.txt, operation abort")

# Function to delete a slot
def deleteSlot():
    slots = readSlot()
    printSlots(slots)

    while True:
            slotNum = int(onlyDigit(input("Enter the number corresponding to the slot you want to delete (or enter 0 to exit): ")))
            if slotNum == 0:
                print("Exiting delete mode!\n")
                return
            elif slotNum < 1 or slotNum > len(slots):
                print("Invalid slot number! Please enter a valid slot number.\n")
            else:
                break

    slotToDelete = slots[slotNum - 1]
    slotToPrint = [slotToDelete]
    print("Deleting the following slot:")
    printSlots(slotToPrint)

    confirmation = input("Are you sure you want to delete this slot?\nEnter 'yes' to delete: ").lower()
    if confirmation == "yes":
        del slots[slotNum - 1]
        writeSlotFile(slots)
        print("Slot deleted successfully!!!\n")
    else:
        print("Deletion cancelled.\n")

# Function to print slots based on their status
def printSlotByStatus(slots = None,status = None):
    if slots == None:
        slots = readSlot()

    if status == None:
        while True:
            status = input("Enter the STATUS you are searching for:[\"ACTIVE\", \"INACTIVE\", \"COMPLETED\"] ").upper()
            if status not in ["ACTIVE", "INACTIVE", "COMPLETED"]:
                print("Invalid status! Choose again:(")
            else:
                break

    slotsByStatus = [slot for slot in slots if slot["STATUS"] == status]
    if len(slotsByStatus):
        printSlots(slotsByStatus)
        return slotsByStatus
    else:
        print("No slot with {} status found :(".format(status))

# Function to print slots based on their booking status
def printSlotByBookingStatus(slots = None,status=None):
    if slots == None:
        slots = readSlot()

    if status == None:
        while True:
            status = input("Enter the STATUS you are searching for:[\"BOOKED\", \"AVAILABLE\",\"CANCELLED\"] ").upper()
            if status not in ["BOOKED", "AVAILABLE","CANCELLED"]:
                print("Invalid booking status! Choose again:(")
            else:
                break

    slotsByBookingStatus = [slot for slot in slots if slot["BOOKING STATUS"] == status.upper()]
    if len(slotsByBookingStatus):
        printSlots(slotsByBookingStatus)
        return slotsByBookingStatus
    else:
        print("No slot with {} status found :(".format(status.upper()))

# Function to print slots based on the launch vehicle
def printSlotsByRocket(slots = None,rocketName = None):
    if slots == None:
        slots = readSlot()

    if rocketName == None:
        rocket = [i for i in specsDict()]
        while True:
            # printing the name to rocket
            for i, j in enumerate(rocket):
                print(i + 1, ".", j, sep="")

            choice = onlyDigit(input("\nChoose the Launch Vehicle: "))
            if int(choice) > 0 and int(choice) <= len(rocket):
                rocketName = rocket[int(choice) - 1]
                print('')
                break
            else:
                print("Invalid choice entered\n")
        print("You chose {}.\n".format(rocketName))

    #sdrach

    slotsByRocket = [slot for slot in slots if slot["LAUNCH VEHICLE"] == rocketName]
    if len(slotsByRocket):
        printSlots(slotsByRocket)#
        return slotsByRocket
    else:
        print("No slot with {} launch vehicle found :(\n".format(rocketName.upper()))

# Function to print slots based on the month of launch
def printSlotsByMonth(slots = None,dateStr = None):
    if slots == None:
        slots = readSlot()

    if dateStr == None:
        while True:
            year = onlyDigit(input("Enter the year:"))
            if  int(year) > 9999 or int(year) < 2024:
                print("Enter a valid year between 2024 and 9999:")
            else:
                dateStr = year + '-'
                break

        while True:
            month = onlyDigit(input("Enter the month:"))
            if int(month) < 1 and int(month) > 12:
                print("Enter a valid month!")
            else:
                dateStr += month
                break

    date = datetime.strptime(dateStr,"%Y-%m")
    slotsByMonth = [slot for slot in slots if date.month == (datetime.strptime(slot["DATE"],"%Y-%m-%d")).month and date.year == (datetime.strptime(slot["DATE"],"%Y-%m-%d")).year]
    if len(slotsByMonth):
        printSlots(slotsByMonth)
        return slotsByMonth
    else:
        print("No slot in {} is available :(".format(dateStr))

# Function to print slots based on the destination
def printByOrbit(slots = None,orbit = None):
    if slots == None:
        slots = readSlot()

    if orbit == None:
        while True:
            orbit = input("Enter the DESTINATION you are searching for:[\"LEO\", \"GTO\", \"SSO\"] ").upper()
            if orbit not in ["LEO", "GTO", "SSO"]:
                print("Invalid orbit! Choose again:(")
            else:
                break
    slotsByOrbit=[slot for slot in slots if slot["DESTINATION"] == orbit]

    if len(slotsByOrbit):
        printSlots(slotsByOrbit)
        return slotsByOrbit
    else:
        print("No slot for {} found! :(".format(orbit))

# Function to log booking history
def bookingHistory(slot):
    s = ''
    with open("booking_history.txt", "a") as fp:
        for i in slot:
            s += i + "~" + slot[i] + "|"
        s += "\n"
        fp.write(s)

# Function to log user booking history
def userBookingActive(username, slots, mode='a'):
    if type(slots)!= list:
        slots=[slots]
    s = ''
    with open(username + "_active_booking.txt", mode) as fp:
        for slot in slots:
            for i in slot:
                s += i + "~" + slot[i] + "|"
            s += "\n"
            fp.write(s)


def userBookingHistory(username,slot):
    s = ''
    with open(username+"_history.txt", "a") as fp:
        for i in slot:
            s += i + "~" + slot[i] + "|"
        s += "\n"
        fp.write(s)

# Function to book a slot
def bookSlot(slots=None,username1=None):
    if username1 == None:
        global username
        username1=username

    if slots == None:
        slots = readSlot()
        slots=dynamicPrice(slots)

    printSlots(slots)

    try:
        while True:
                num=int(onlyDigit(input("Enter the number corresponding to the slot you want to book (or enter 0 to exit): ")))
                if num==0:
                    print("Exiting booking mode!!\n")
                    return
                elif num < 1 or num > len(slots):
                    print("Invalid slot number! Please enter a valid slot number.")
                else:
                    break
    except ValueError:
        print("Invalid slot entered, cannot process further:(\n")
        return
    except:
        print("Some error occurred, cannot book the slot\n")
        return

    payloadName = input("Enter payload name:")

    if  slots[num - 1]["BOOKING STATUS"] != "AVAILABLE"  or  slots[num - 1]["STATUS"] != "ACTIVE":
        print("Chosen slot not available, booking failed !\n")
        return
    #updating booking status in launch slot file
    updateBookingStatus(slots[num - 1], "BOOKED")
    slots[num - 1]["BOOKING STATUS"] = "BOOKED"
    bookedSlot = slots[num - 1]
    bookedSlot.update(
        {
            "TIME": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "PAYLOAD": payloadName,
        }
    )
    # updating booking details in user history
    userBookingHistory(username1, bookedSlot)
    userBookingActive(username1, bookedSlot)
    bookedSlot.update({"USERNAME": username1})

    # updating booking details in server history
    bookingHistory(bookedSlot)

    # updating booking count in user profile
    profile = readProfile(username1)
    count = int(profile[username1]["PAST BOOKINGS"]) + 1
    profile[username1]["PAST BOOKINGS"] = str(count)
    writeProfile(username1, profile)

    addRemark(username1,'Booking of slot DATE:' + bookedSlot['DATE'] + ' with payload ' + bookedSlot['PAYLOAD'] + ' to ' + bookedSlot['DESTINATION'] + ' done at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.')

    print("Booking Successful!!!")

# Function to cancel a booking
def cancelBooking(username1=None):
    if username1 == None:
        global username
        username1 = username

    #fetch history
    try:
        userBookings=readSlot(username1+"_active_booking.txt")

        if len(userBookings) == 0:
            print("You don't have any bookings to cancel.")
            return
        printSlots(userBookings)
    except :
        print("You don't have any bookings to cancel.")
        return
    num=None


    try:
        while True:
            num = int(onlyDigit(input("Enter the number corresponding to the slot you want to cancel (or enter 0 to exit): ")))
            if num == 0:
                print("Exiting canceling mode!")
                return
            elif num < 1 or num > len(userBookings):
                print("Invalid slot number! Please enter a valid slot number.")
            else:
                break
    except ValueError:
        print("Invalid slot entered, cannot process further:(")
        return
    except:
        print("Error occurred, cannot failed canceling slot!!! ")
        return

    # to check if the slot is already cancelled
    if userBookings[num-1]["BOOKING STATUS"] == "CANCELED":
        print("Chosen slot is already canceled, redirecting back.")
        return
    elif userBookings[num-1]["BOOKING STATUS"] == "BOOKED" and userBookings[num-1]["STATUS"] == "ACTIVE":
        userBookings[num-1]["BOOKING STATUS"] = "CANCELED"
    else:
        print("Chosen slot is already canceled , redirecting back.")
        return


    printSlots([userBookings[num - 1]])
    confirmation = input("Enter 'yes' if you want to save BOOKING STATUS of selected slot: ").upper()
    if confirmation != "YES":
        print("Abort cancellation ")
        return

    userBookings[num - 1]["TIME"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    userBookingHistory(username1,userBookings[num-1])
    addRemark(username1,'Booking canceled of slot DATE:'+userBookings[num - 1]['DATE']+' with payload '+userBookings[num - 1]['PAYLOAD'] +' to '+userBookings[num - 1]['DESTINATION']+' at '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.')
    userBookings[num - 1].update({"USERNAME": username1})
    bookingHistory(userBookings[num - 1])
    del userBookings[num-1]["USERNAME"]
    del userBookings[num - 1]["PAYLOAD"]
    del userBookings[num - 1]["TIME"]

    userBookings[num - 1]["BOOKING STATUS"] = "BOOKED"
    updateBookingStatus(userBookings[num - 1], "AVAILABLE")
    del userBookings[num - 1]
    userBookingActive(username=username1, slots = userBookings, mode='w')
    print("Selected slot cancelled")

#Function to display booking history
def displayBookingsHistory(username = None):
    filename=''
    if username == None:
        filename = "booking_history.txt"
    else:
        filename = username + "_history.txt"
    slots = readSlot(filename)
    if slots == None or len(slots)==0:
        print("No booking history found.")
        return
    while True:
        print("1. View All History\n2. Search History via Keywords\n3. Exit\n")

        choice = input("Enter your choice :")

        if choice == '1':
            print("Printing Complete Booking History...")
            printSlots(slots)
            return
        elif choice == '2':
            print("Search Menu opening...")
            search(slots=slots)
            return
        elif choice == '3':
            print('Exiting...')
            return
        else:
            print("Invalid Choice Entered")

# Function to update launch completion status
def updateLaunchCompletion(username=None):
    current = datetime.now()
    testDate = datetime.strptime("2025-9-27", "%Y-%m-%d")
    #TODO  swap current date with test date before running
    try:
        slots=readSlot()
        for slot in slots:
            date1 = datetime.strptime(slot["DATE"], "%Y-%m-%d")
            if current> date1 :
                slot["STATUS"] = "COMPLETED"
        writeSlotFile(slots)#upsating status in slot file
    except:
        print('')


    try:
        slots = readSlot("booking_history.txt")
        for slot in slots:
            date1 = datetime.strptime(slot["DATE"], "%Y-%m-%d")
            if current > date1:
                slot["STATUS"] = "COMPLETED"
                bookingHistory(slot) #apending booking history
    except:
        print('')


    if username != None:
        try:
            slots = readSlot(username+"_history.txt")
            for slot in slots:
                date1 = datetime.strptime(slot["DATE"], "%Y-%m-%d")
                if current > date1:
                    slot["STATUS"] = "COMPLETED"
                    userBookingHistory(username,slot) #appending user booking history file
        except:
            print('')

        try:
            slots = readSlot(username+"_active_booking.txt")
            for slot in slots:
                date1 = datetime.strptime(slot["DATE"], "%Y-%m-%d")
                if current > date1:
                    slot["STATUS"] = "COMPLETED"
                    addRemark(username, slot['LAUNCH VEHICLE'] + ' launched at '+ slot['DATE']+' with payload '+slot['PAYLOAD'] +' to '+slot['DESTINATION']+'.')
            userBookingActive(username,slots,'w') #writing user booking history file
            addRemark(username,'')
        except:
            print('')
