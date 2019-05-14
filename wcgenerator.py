import random
from wcnaming import *
from wcprofile import *

def generateNameList():
    while True:
        numnames = input("How many names to generate? ")
        try:
            numnames = int(numnames)
        except:
            print("Invalid input. Please enter a number.")
            continue
        break

    for x in range(0, numnames):
        name = generateName()
        print(name)


def generateProfiles():
    while True:
        numcats = input("How many cats to generate?  ")
        numtraits = input("How many personality traits per cat?  ")
        print()

        try:
            numcats = int(numcats)
            numtraits = int(numtraits)
        except:
            print("Invalid input. Please enter a number.")
            continue
        break

    for x in range(0, numcats):
        role = generateRole()
        name = generateName(role)
        gender, pronoun = generateGender(role)
        personality = generatePersonality(numtraits)
        secret = generateSecret(role)
        addtl = generateAdd()

        print(name + " is a " + gender + " " + role + ". Others describe " + pronoun + " as " + ', '.join(personality) + ".")
        if(secret !="" and addtl != ""):
            print(name + " " + secret + " and " + addtl + ".")
        else:
            if(secret != ""):
                print(name + " " + secret + ".")
            if(addtl != ""):
                print(name + " " + addtl + ".")

        print()

# generate a clan's worth of characters
# one leader, one deputy, one medicine cat, 15 warriors, 5 queens, 5 elders, 7 apprentices, 9 kits
def generateClan(traits=3):
    clanRoles = ['leader', 'deputy', 'medicine cat']
    warriors = ['warrior'] * 15
    queens = ['queen'] * 5
    elders = ['elder'] * 5
    apprentices = ['apprentice'] * 7
    kits = ['kit'] * 9

    # complete list of roles for a Clan
    clanRoles = clanRoles + warriors + queens + elders + apprentices + kits

    for i in range(0, len(clanRoles)):
        role = clanRoles[i]
        gender, pronoun = generateGender(role)
        name = generateName(role)
        personality = generatePersonality(traits)
        addtl = generateAdd()
        secret = generateSecret(role)

        # kits and apprentices shouldn't have secrets

        print(name + " is a "+ gender + " " + role+ ". Others describe " + pronoun + " as " + ', '.join(personality) + ".")
        if(secret !="" and addtl != ""):
             print(name + " " + secret + " and " + addtl + ".")
        else:
             if(secret != ""):
                 print(name + " " + secret + ".")
             if(addtl != ""):
                 print(name + " " + addtl + ".")
        print()

def main():

    # ask user what they want to generate?
    while True:
        whatGenerate = input("What would you like to generate? \n Press 1 to generate names only \n Press 2 to generate character profiles \n Press 3 to generate a Clan of characters\n")
        try:
            whatGenerate = int(whatGenerate)
        except: # handles case where whatGenerate is not a number
            print("Invalid input. Please try again:")
            continue
        if whatGenerate not in [1, 2, 3]: # handles case if number entered is invalid
            print("Invalid input. Please try again:")
            continue
        else:
            break

    if(whatGenerate == 1):
        # generate adult names only
        generateNameList()
        return

    if(whatGenerate == 2):
        # generate character profiles
        generateProfiles()
        return

    if(whatGenerate == 3):
        # generate clan of characters
        generateClan()
        return




if __name__ == "__main__":
    main()
