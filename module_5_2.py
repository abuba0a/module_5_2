class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.floors = floors
        House.numberOfFloors = floors
        print(House.numberOfFloors)


Floor = House(0)
Floor.setNewNumberOfFloors(78)
