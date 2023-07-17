def greet_it(func): # decorator in python
    def wrapper(): 
        print("Greetigs")
        func()
        print("Goodbye")
    return wrapper

# using decorator to be used before each function
@greet_it
def add_it():
    print("Add function")

@greet_it
def sub_it():
    print("Subtraction function")

add_it()
sub_it()