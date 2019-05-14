import random
prefixfile = "prefix.txt"
suffixfile = "suffix.txt"

# randomly generates prefix of name from prefix.txt
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

# randomly generates suffix of name from suffix.txt
def generateSuffix():
    suffix = []
    with open(suffixfile, 'r') as suffixes:
        for line in suffixes:
            fields = line.strip('\n').split(",")
            for s in fields:
                suffix.append(s)
    suffixindex = random.randint(0, len(suffix)-1)
    return suffix[suffixindex]


# generates name from generatePrefix() and generateSuffix()
# accounts for special naming rules for leaders, apprentices, kits
# ensures that prefix != suffix and accounts for hyphenated names
def generateName(role='warrior'):
    prefix = generatePrefix()
    suffix = generateSuffix()

    # special name generation rules
    if(role == 'leader'):
        return generateNameLeader();
    if (role == 'apprentice'):
        return generateNameApprentice();
    if (role == 'kit'):
        return generateNameKit();

    while (prefix.lower()==suffix): # don't allow prefix and suffix to match
        suffix = generateSuffix() # reroll suffix

    if (prefix[-1:] == suffix[:1]): # if last char of prefix and first char of suffix match
        name = prefix + '-' + suffix # put a '-' between them
    else:
        name = prefix + suffix
    return name

# generates name with -star suffix for leader and in parenthesis, their warrior name
# accounts for hyphenated names
def generateNameLeader():
    prefix = generatePrefix()
    suffix = generateSuffix()

    warriorname = prefix + suffix
    leadername = prefix + 'star'

    if (prefix[-1:] == suffix[:1]): # if last char of prefix and first char of suffix match
        warriorname = prefix + '-' + suffix # put a '-' between them

    if (prefix[-1:] == 's'):
        leadername = prefix + '-star'

    name = leadername + " (" + warriorname + ")"
    return name

# generates name with -paw suffix for apprentices and in parenthesis, their warrior name
# accounts for hyphenated names
def generateNameApprentice():
    prefix = generatePrefix()
    suffix= generateSuffix()

    warriorname = prefix + suffix
    apprenticename = prefix + 'paw'

    if (prefix[-1:] == suffix[:1]): # if last char of prefix and first char of suffix match
        warriorname = prefix + '-' + suffix # put a '-' between them

    if (prefix[-1:] == 'p'):
        apprenticename = prefix + '-paw'

    name = apprenticename + " (" + warriorname + ")"
    return name


# generates name with -kit suffix for kits and in parenthesis, their warrior name
# accounts for hyphenated names
def generateNameKit():
    prefix = generatePrefix()
    suffix = generateSuffix()

    warriorname = prefix + suffix
    kitname = prefix + 'kit'

    if (prefix[-1:] == suffix[:1]):
        warriorname = prefix + '-' + suffix
    if (prefix[-1:] == 'k'):
        kitname = prefix + '-kit'

    name = kitname + " (" + warriorname +")"
    return name

# test functions here
def main():
    print(generateNameLeader())
    print(generateNameApprentice())
    print(generateNameKit())
    for i in range(0, 10):
        print(generateName(role='kit'))
        print(generateName(role='apprentice'))
        print(generateName(role='warrrior'))
        print(generateName(role='leader'))

if __name__ == "__main__":
    main()
