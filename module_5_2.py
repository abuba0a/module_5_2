class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.floors = floors
        numberOfFloors = floors
        print(numberOfFloors)


Floor = House(0)
Floor.setNewNumberOfFloors(78)
