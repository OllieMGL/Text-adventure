class Location:
    #ATTRIBUTES
    #description - Str
    #inventory - list
    #directions - dict
    #enemies - list
    
    def __init__(self,
                 description: 'String', 
                 inventory: 'list' = [], 
                 enemies: 'list' = []):
        self.description = description
        self.inventory = inventory
        self.enemies = enemies    
    
    #Set the directions attribute of the object
    def setDirections(self, directions: 'dict'):
        self.directions = directions
        