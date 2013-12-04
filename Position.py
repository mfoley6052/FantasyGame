#Mitchell Foley
class position():

    def __init__(self,inUse,item):
        self.inUse = inUse
        self.item = item

    def getState(self):
        return self.inUse

    def getItem(self):
        return self.item

    def equip(self,obj):
        self.inUse = 1
        self.item = obj
    
        
    
