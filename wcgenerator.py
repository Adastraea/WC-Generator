import random

prefixfile = "prefix.txt"
suffixfile = "suffix.txt"
personalityfile = "personality.txt"
secretfile = "secret.txt"
addtlfile = "additional.txt"


def generatePrefix():
    prefix = []
    name = ""
    with open(prefixfile, 'r') as prefixes:
        for line in prefixes:
            fields = line.strip('\n').strip(' ').split(",")
            for p in fields:
                prefix.append(p)
    prefixindex = random.randint(0, len(prefix)-1)
    return prefix[prefixindex]

def generateSuffix():
    suffix = []
    with open(suffixfile, 'r') as suffixes:
        for line in suffixes:
            fields = line.strip('\n').split(",")
            for s in fields:
                suffix.append(s)
    suffixindex = random.randint(0, len(suffix)-1)
    return suffix[suffixindex]

def generateName():
    prefix = generatePrefix()
    suffix = generateSuffix()

    while (prefix.lower()==suffix): # don't allow prefix and suffix to match
        suffix = generateSuffix() # reroll suffix

    if (prefix[-1:] == suffix[:1]): # if last char of prefix and first char of suffix match
        name = prefix + '-' + suffix # put a '-' between them
    else:
        name = prefix + suffix
    return name

def generatePersonality(number):
    traits = []
    catTraits = []
    with open(personalityfile, 'r') as personality:
        for line in personality:
            fields = line.strip('\n').split(",")
            for t in fields:
                traits.append(t)

    for i in range(0, number):
        traitindex = random.randint(0, len(traits)-1)
        trait = traits[traitindex]
        catTraits.append(trait)
        traits.remove(trait)
    return catTraits

def generateGender():
    gender = ['male', 'female', 'non-binary']
    genderindex = random.randint(0, len(gender)-1)
    return gender[genderindex]

def generateSecret():
    secrets = []
    secretTest = random.random()
    if(secretTest < 0.75):
        return ""

    with open(secretfile, 'r') as sec:
        for line in sec:
            fields = line.strip('\n').split(",")
            for s in fields:
                secrets.append(s)
    secretindex = random.randint(0, len(secrets)-1)
    return secrets[secretindex]

def generateRole():
    roles = ["medicine cat", "leader", "deputy", "queen", "elder"]
    roleIndex = random.randint(0, len(roles)-1)
    return roles[roleIndex]

def generateAdd():
    addtls = []
    addTest = random.random()
    if(addTest < 0.90):
        return ""

    with open(addtlfile, 'r') as add:
        for line in add:
            fields=line.strip('\n').split(",")
            for a in fields:
                addtls.append(a)
    addtlsIndex = random.randint(0, len(addtls)-1)
    return addtls[addtlsIndex]


def main():
    numcats = input("How many cats to generate?  ")
    numtraits = input("How many personality traits per cat?  ")
    print()

    numcats = int(numcats)
    numtraits = int(numtraits)

    for x in range(0, numcats):
        name = generateName()
        role = generateRole()
        gender = generateGender()
        personality = generatePersonality(numtraits)
        #personality = (', '.join(personality))
        secret = generateSecret()
        addtl = generateAdd()

        print(name + " is a " + gender + " " + role + ". Others describe them as " + ', '.join(personality) + ".")
        if(secret !="" and addtl != ""):
            print(name + " " + secret + " and " + addtl + ".")
        else:
            if(secret != ""):
                print(name + " " + secret + ".")
            if(addtl != ""):
                print(name + " " + addtl + ".")

        print()

if __name__ == "__main__":
    main()
