class DevBoards:
    # a constructor is a special method in a class, that is used to CREATE AND INITIALIZE an object
    def __init__(self, bName, bModel) -> None:
        self.name = bName
        self.model = bModel
    def boardDetail(self):
        print(f"{self.name} has model {self.model}")



board1 = DevBoards("Arduino", 2018) # constructor will be called automatically whenever we create an object
board1.boardDetail()
board2 = DevBoards("Raspberry", 2022)
board2.boardDetail()
