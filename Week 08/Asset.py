class Asset:
    def __init__(self, tag, mac, sn, mn, owner):
        self.AssetTag = tag
        self.MacAddress = mac
        self.SerialNumber = sn
        self.ModelNumber = mn
        self.Owner = owner

    def toString(self):
        rtnStr = "{0}\n\tSerial Number: {1}\n\tModel Number: {2}\n\tMac Address: {3}\n\tOwner: {4}"
        return rtnStr.format(self.AssetTag, self.SerialNumber, self.ModelNumber, self.MacAddress, self.Owner)

