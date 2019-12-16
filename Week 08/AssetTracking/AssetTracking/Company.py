from Location import *
from Asset import *

class Company:
    def __init__(self, name):
        self.Name = name
        self.Locations = list()
    
    def AddLocation(self, locationName):
        self.Locations.append(Location(locationName))

    def GetLocations(self):
        locNames = list()
        for loc in self.Locations:
            locNames.append(loc.Name)
        return locNames

    def FindLocation(self, locationName):
        index = self.GetLocations().index(locationName)
        if index != None:
            return self.Locations[index]

    def GetAllAssetsAt(self, LocationName):
        location = self.FindLocation(LocationName)
        if location != None:
            return location.GetAllAssets()

    def GetAsset(self, assetTag):
        for loc in self.Locations:
            a = loc.GetAsset(assetTag) 
            if a != None:
                return a
