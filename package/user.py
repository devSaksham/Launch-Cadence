import time
import sys

def addRemark(username,string):
    with open(username+'_remark.txt','a') as fp:
        fp.write(string+"\n")

def readRemark(username):
    with open(username + '_remark.txt', 'r') as fp:
        return fp.readlines()

def printRemark(username):
    lines = readRemark(username)
    for line in lines:
        print('->',line.strip('\n'))
    print('')

def getUser():
    user={}
    try:
        with open("user.txt","r") as fp:
            lines=fp.readlines()
            if len(lines)!=0 :
                for line in lines:
                    line=line.strip("\n")
                    k=line.split(':')
                    user.update({k[0]:k[1]})
    except:
        print('',end='')
    return user

def writeUser(user):
    with open("user.txt","w") as fp:
        for i in user.keys():
            fp.write(i+":"+user[i]+'\n')

def validEmail():
    email="test"

    while (('@' or '.com' not in email) or '@.com' in email):
        email=input("Enter your email :")
        if ('@' and '.com' in email) and ('@.com' not in email):     #checking if the mail is valid
            return email
            break
        else:
            print("Enter valid email !!!")

def validPhone():
    number='0000'
    while len(number)!=10 or number.isdigit()==False:
        number=input("Enter your phone number: ")
        if number.isdigit()== False:
            print("ONLY DIGITS ALLOWED\n")
        elif len(number)!=10:
            print("kindly enter 10 digits\n")
        else:
            return number

def addUser():
    user=getUser()
    with open("user.txt","a") as fobj:
        username=''
        while(True):
            username=input("Enter user name: ")
            if username in user:
                print("username already exists\n")
            elif " " in username:
                print("Whitespace not allowed")
            else:
                break  
        pwd=input("Enter password :")
        with open(username+".txt","w") as fp:
            info={
                "NAME":input("Enter Your Name: "),
                "PHONE NUMBER":validPhone(),
                "EMAIL":validEmail(),
                "GENDER":input("Enter your gender:"),
                "ORGANISATION NAME":input("Enter the name of organisation: "),
                "ADDRESS":input("Enter address: "),"COUNTRY":input("Enter country: "),
                "FIRST LOGIN":time.strftime("%Y-%m-%d %H hrs %M min %S sec", time.localtime()),
                "PAST BOOKINGS":"0"
            }
            for i in info:
                fp.write(i+":"+info[i]+"\n")
        fobj.write(username+":"+pwd+"\n")
    print("User created successfully!!! :)")
    addRemark(username,"Profile created at "+time.strftime("%Y-%m-%d %H hrs %M min %S sec", time.localtime()))

def readProfile(username):
    profile={}
    info={}
    with open(username+".txt","r") as fp:
        for line in fp.readlines():
            k=(line.strip("\n")).split(':')
            info.update({k[0]:k[1]})
        profile={username:info}
    return profile

def displayProfile(username):
    profile=readProfile(username)
    print("Username :",username)
    for i in profile[username]:
        print(i+" : "+profile[username][i])
    print('\n')

def writeProfile(username,profile):
    with open(username+".txt","w") as fp:
        info={}
        info.update(profile[username])
        for i in info:
            fp.write(i+":"+info[i]+"\n")

def deleteUser(username):
    user=getUser()
    ch = input("do you want to delete {} user if no then press 0 else enter 1:".format(username))
    if ch.isdigit():
        if int(ch)==0:
            print("abort deleting.")
        elif int(ch)== 1:
            user.pop(username)
            writeUser(user)
        else:
            print("Invalid input entered.")
            return
    else:
         print("Invalid input entered.")
         return
    print("{} deleted successfully!!\n".format(username))
    print("\nExiting...\nTHANK YOU FOR COMING!!!\nProgram Successfully Closed :)")
    addRemark(username,'User profile deleted at '+time.strftime("%Y-%m-%d %H hrs %M min %S sec", time.localtime()))
    sys.exit()
        
def updateProfile(username):
    profile=readProfile(username)
    info=profile[username]
    while(True):
        displayProfile(username)
        var=(input("Enter the info you want to update or 0 to exit: ")).upper()
        if var =='0':
             print("Exited\n")
             break
        elif var=="USERNAME":
             print("Sorry,it cannot be changed :(\n")
        elif var in info:
            if var == "EMAIL":
                info[var]=validEmail()
                profile={username:info}
                writeProfile(username,profile)
                addRemark(username,"Email updated at" +time.strftime("%Y-%m-%d %H hrs %M min %S sec", time.localtime()))
            elif var == "PHONE NUMBER":
                info[var]=validPhone()
                profile={username:info}
                writeProfile(username,profile)
                addRemark(username,'Phone Number updated at'+time.strftime("%Y-%m-%d %H hrs %M min %S sec", time.localtime()))
            elif var=="FIRST LOGIN" or"PAST BOOKINGS":
                print("Sorry,it cannot be changed :(\n")
            else:
                info[var]=input("Enter new information :")
                profile={username:info}
                writeProfile(username,profile)
                addRemark(username,var+' updated at '+time.strftime("%Y-%m-%d %H hrs %M min %S sec", time.localtime()))
                print("")

        else:
            print("Enter valid input")

