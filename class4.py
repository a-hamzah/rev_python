class Computer:
    def config(self):
        print("i5, 7th Gen, tower")

comp1 = Computer()

# Computer.config(comp1)
comp1.config()

# ----------


class Computer:
    def config(self, type):
        print("i5, 7th Gen, tower")
        print(type)

comp1 = Computer()

Computer.config(comp1, "standard")