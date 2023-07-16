class Person:
    name = "Scott" # attributes of class
    occupation = "Carpenter" 
    networth = 10 

    def cons1(self): # methods of class
        print(f"{self.name} is a {self.occupation} with worth {self.networth}")
    def cons2(self):
        print("Hello from 2nd Method")

a1 = Person() # creating object of class
a2 = Person()

print(a1.name) # calling attributes of class through object
print(a1.occupation)
print(a1.networth)

a1.cons1() # calling methods of class through object
a1.cons2()

a2.name = "Chris"
a2.occupation = "Coach"
a2.networth = 20
a2.cons1()
a2.cons2()
