from random import *
from Company import *
from getpass import getuser

#random serialnumber for random asset generation
def randomSN():
    sn = "{0}{1}{2}{3}{4}{5}{2}{5}{3}{1}{0}{4}".format(randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
    return sn

#random model number for random asset generation
def randomModel():
    mn = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(randChar(), randChar(), randChar(), randChar(), randChar(), randChar(), randChar(), randChar(), randChar(), randChar())
    return mn


#random alpha character A-Z
def randAlphabet():
    return chr(randint(65,90))

#random alphanumberic character A-Z or 0-9
def randChar():
    num = randint(0,1)
    if num == 0:
        return randAlphabet()
    else:
        return randint(0,9)

#Random Mac Address for random asset generation
def randomMAC():
    #XX-XX-XX-XX-XX-XX
    mac = "{0}{1}-{2}{3}-{4}{5}-{6}{7}-{8}{9}-{10}{11}".format(randChar(),randChar(),randChar(),randChar(),randChar(),randChar(),randChar(),randChar(),randChar(),randChar(),randChar(),randChar())
    return mac

def addSubLocations(location, numLocations):
    print(location.Name)
    manualEntry_L = bool(int(input("Would you like to manually enter sublocation names?(1:Yes, 0:No): ")))
    for x in range(numLocations):
        locName = "{0}_{1}".format(location.Name, x)
        if manualEntry_L:
            locName = input("Please enter a location name:")
        location.AddSubLocation(locName)

    for x in location.SubLocations:
        numLocations = int(input("How Many SubLocations Does {0} have?: ".format(x.Name)))
        if numLocations > 0:
            addSubLocations(x,numLocations)



def main():
    companyName = input("Enter a Company Name: ")
    company = Company(companyName)
    numLocations = int(input("How Many Locations Does {0} have?: ".format(companyName)))
    manualEntry_L = bool(int(input("Would you like to manually enter location names?(1:Yes, 0:No): ")))
    for x in range(numLocations):
        locName = "TestLocation_{0}".format(x)
        if manualEntry_L:
            locName = input("Please enter a location name:")
        company.AddLocation(locName)

    for x in company.Locations:
        numSubLocations = int(input("How Many SubLocations Does {0} have?: ".format(x.Name)))
        if numSubLocations > 0:
            addSubLocations(x,numSubLocations)

    for loc in company.Locations:
        numAssets = int(input("How Many Assets at location {0}?: ".format(loc.Name)))
        assetEntryMode = int(input("How would you like to enter assets? (1: Manually, 2: Names Only, 3: Randomly): "))
        for x in range(numAssets):
            mn = randomModel()
            sn = randomSN()
            mac = randomMAC()
            owner = getuser()
            tag = "Device_{0}".format(x)

            if assetEntryMode != 3:
                tag = input("Enter an asset tag for {0}: ".format(tag))
                if assetEntryMode == 1:
                    mn = input("Enter the {0}: ".format("Model Number"))
                    sn = input("Enter the {0}: ".format("Serial Number"))
                    mac = input("Enter the {0}: ".format("MAC Address"))
                    owner = input("Enter the {0}: ".format("Owner"))

            loc.Assets.append(Asset(tag,mac,sn,mn,owner))
    print("\n")
    print(company.Name)
    for l in company.GetLocations():
        print(l)

    locName = input("\nEnter a Location to see a list of Assets from that location: ")
    for a in company.GetAllAssetsAt(locName):
        print(a)

    tag = input("\nEnter an Asset Tag to get details about that asset: ")
    print(company.GetAsset(tag).toString())


main()