class Boards:
    name = "Arduino"
    functionality = "no wifi"
    version = 1.2
    def devboards(self):
        print(f"{self.name} has {self.functionality} and its version is {self.version}")

board1 = Boards()
board1.devboards()

board2 = Boards()
board2.name = "raspberry pi"
board2.functionality = "wifi"
board2.version = 3
board2.devboards()