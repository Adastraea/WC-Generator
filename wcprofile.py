import random
personalityfile = "personality.txt"
secretfile = "secret.txt"
addtlfile = "additional.txt"


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

def generateGender(role='warrior'):
    # genders and their probabilities weights can be modified here
    gender = ['male'] *40 + ['female']*40 + ['non-binary']*20
    index = random.randint(0, len(gender)-1)

    # queens should probably be mostly female, but allow for NB/trans characters as well
    if(role=='queen'):
        gender = ['male'] *10 + ['female']*80 + ['non-binary']*10
        index = random.randint(0, len(gender)-1)

    charGender = gender[index]
    if(charGender == 'male'): pronoun = 'him'
    if(charGender == 'female'): pronoun = 'her'
    if(charGender == 'non-binary'): pronoun = 'them'

    return charGender, pronoun

def generateSecret(role='warrior'):
    # kits and apprentices don't have secrets
    if(role=='kit' or role=='apprentice'):
        return ""

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
    roles = ["medicine cat", "leader", "deputy", "queen", "elder", "kit", "apprentice"]
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
