from package.user import *

def onlyDigit(x):
    while True:
        if x.isdigit():
            return x
        else:
            print("Only digits allowed!!!")
            x=input("Enter the number again:")
def writePrice(price):
    with open("price.txt","w") as fp:
        for i in price:
            s=""
            s=str(i)+"-"
            for j in price[i]:
                s+=str(j)+":"+price[i][j]+"|"
            s+='\n'
            fp.write(s)
def writeSpecs(specs):
    with open("spec.txt","w") as fp:
        for name in specs:
            s=""
            s=str(name)+"-"
            for j in specs[name]:
                s+=j+":"+specs[name][j]+"|"
            s+="\n"
            fp.write(s)
def appendPrice(price):
    with open("price.txt","a") as fp:
        for i in price:
            s=""
            s=str(i)+"-"
            for j in price[i]:
                s+=str(j)+":"+price[i][j]+"|"
            s+='\n'
            fp.write(s)
def appendSpecs(specs):
    with open("spec.txt","a") as fp:
        for name in specs:
            s=""
            s=str(name)+"-"
            for j in specs[name]:
                s+=j+":"+specs[name][j]+"|"
            s+="\n"
            fp.write(s)
def priceDict():
    price={}
    with open("price.txt","r") as fp:
        lines=fp.readlines()
        for line in lines:
            k=line.split('-')
            l=k[1].split('|')
            l.pop()
            d1=dict()
            for i in l :
                d1.update({i.split(':')[0]:i.split(':')[1].strip('\n')})
            price.update({k[0]:d1})
    return price
def specsDict():
    specs={}
    with open("spec.txt","r") as fp:
        lines=fp.readlines()
        for line in lines:
            k=line.split('-')
            l=k[1].split('|')
            l.pop()
            d1=dict()
            for i in l :
                d1.update({i.split(':')[0]:i.split(':')[1].strip('\n')})
            specs.update({k[0]:d1})
    return specs

#Unit testing done
def addRocket():
    specs=specsDict()
    
    rName=(input("Enter name of rocket: ")).upper()
    if rName in specs:
        print("Launch Vehicle already exists.")
        return
    else:
        d1={
            "COUNTRY":input("Enter country origin: "),
            "HEIGHT":onlyDigit(input("Enter height of launch vehicle(in meters): "))+ ' m',
            "WIDTH":onlyDigit(input("Enter width or diameter of launch  vehicle(in meters): "))+" m",
            "MASS":onlyDigit(input("Enter mass (in tons): "))+" ton"
            }
        d2={}
        flag='1'
        while(flag == '1'):
            orbitname=''
            while True:
                orbitname=(input("Enter the name of orbit(SSO,LEO,GTO):")).upper()
                if orbitname in ('SSO','LEO','GTO'):
                    break
                else:
                    print("Invalid orbit entered!!!\n")

            orbit={orbitname:(input("Enter capacity for {}:".format(orbitname))+" tons")}
            d1.update(orbit)
            orbit={orbitname:input("Enter price per kg:(in thousand $)")}
            d2.update(orbit)
            flag=input("Enter 1 if you want add more orbits : ")
    str({rName:d2})
    appendPrice({rName:d2})
    appendSpecs({rName:d1})
    print(f"{rName} added successfully !!!")

#Unit testing done
def displaySpecs():           
    specs=specsDict()
    
    for i,j in enumerate(specs):
        print(i+1,".",j," :",sep="")
        for k,l in specs[j].items():
            print(k,":",l)
        print('')
    print("\n")

#Unit testing done
def displayPrice():
    price=priceDict()
    
    for i,j in enumerate(price):
        print(i+1,".",j," :",sep="")
        for k,l in price[j].items():
            print(k,": $",l,"k per kg",sep="")
        print('')
    print("\n")           

#Unit testing done
def updateSpecs():
    specs=specsDict()
    rocket = [i for i in specs]
    rName=''
    while True:
        # printing the name to rocket
        for i, j in enumerate(rocket):
            print(i + 1, ".", j, sep="")

        choice = onlyDigit(input("\nChoose the Launch Vehicle(0 to exit): "))

        if int(choice) > 0 and int(choice) <= len(rocket):
            rName = rocket[int(choice) - 1]
            print('')
            break
        elif choice == '0':
            print("Exiting...")
            return
        else:
            print("Invalid choice entered\n")


    for spec in specs[rName]:
            print(spec+":"+specs[rName][spec])

    newSpec=(input("Enter the spec you want to update: ")).upper()

    if newSpec in specs[rName].keys():

        # updating the data in dictonary
        if newSpec in('GTO' ,'MASS','LEO','SSO'):
            specs[rName][newSpec] = onlyDigit(input("Enter updated details: "))+' ton'
        elif newSpec in('HEIGHT','WIDTH'):
            specs[rName][newSpec] = onlyDigit(input("Enter updated details: ")) + ' m'
        else:
            specs[rName][newSpec] = input("Enter updated details: ")

    else:
        print(newSpec," does not exist.")
        return

    writeSpecs(specs)
    print("Launch Vehicle Config. Updated Successfully !!!\n")

#Unit testing done
def updatePrice():
    price=priceDict()
    rocket=[i for i in price]
    rName = ''
    while True:
        # printing the name to rocket
        for i, j in enumerate(rocket):
            print(i + 1, ".", j, sep="")

        choice = onlyDigit(input("\nChoose the Launch Vehicle(0 to exit): "))
        if int(choice) > 0 and int(choice)<= len(rocket):
            rName = rocket[int(choice)-1]
            print('')
            break
        elif choice == '0':
            print("Exiting...")
            return
        else:
            print("Invalid choice entered\n")

    print("You chose {}.".format(rName))


    for i in price[rName]:
            print(i,": $",price[rName][i],"k per kg",sep="")

    newPrice=input(("Enter the Orbit name you want to update: ")).upper()

    if newPrice in price[rName].keys():
        price[rName][newPrice]=input("Enter the price in thousand $ per kg: ")
    else:
        print(newPrice," does not exist.")
        return

    writePrice(price)
    print("Price successfully updated!!!\n")

def deleteRocket():
        
    specs=specsDict()
    price=priceDict()
    rocket = [i for i in price]
    rName = ''

    while True:
        # printing the name to rocket
        for i, j in enumerate(rocket):
            print(i + 1, ".", j, sep="")

        choice = onlyDigit(input("\nChoose the Launch Vehicle(0 to exit): "))
        if int(choice) > 0 and int(choice) <= len(rocket):
            rName = rocket[int(choice) - 1]
            print('')
            break
        elif choice == '0':
            print("Exiting...")
            return
        else:
            print("Invalid choice entered\n")
    print("You chose {}.\n".format(rName))

    if rName in price and specs:
        del price[rName]
        del specs[rName]
    else:
        print(rName," does not exist.")
        return
              
    writePrice(price)
    writeSpecs(specs)
    print(f"{rName} Deleted Successfully !!!\n")


def displaySpecsOfParticularRocket(rocket):
    specs=specsDict()
    print("Configuration of {}:".format(rocket))
    for i in specs[rocket]:
        print(i,"->",specs[rocket][i])
