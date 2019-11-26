#A list is a collection of values, sorted or unsorted
#A dictionary is a list of key value pairs.
##The key acts similarly to the index of a list but has unique value

class Computer:
    def __init__(self, sn, name, location):
        self.SerialNumber = sn
        self.Name = name
        self.Location = location
        
    def toDictionary(self):
        rtnDict = {
            "SerialNumber": self.SerialNumber,
            "Name": self.Name,
            "Location": self.Location
            }
        return rtnDict

def main():
    computerList = []
    computerList.append(Computer("8KFTV2596", "L25963", "C410"))
    computerList.append(Computer("9FTLC6578", "L25955", "C411"))
    computerList.append(Computer("7IPHM0231", "L25978", "C413"))
    
    for comp in computerList:
        print(comp.toDictionary())
        
main()
    