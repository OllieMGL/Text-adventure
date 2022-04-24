class Location:
    def __init__(self,description, inventory):
        self.description = description
        self.inventory = inventory
    
    def setDirections(self, directions):
        self.directions = directions
        