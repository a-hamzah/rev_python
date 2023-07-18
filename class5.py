class Polygon:
    def __init__(self, aName, aSides) -> None:
        self.name = aName
        self.sides = aSides
        print(f'{self.name} has {self.sides} sides')

square = Polygon("Square", 4)