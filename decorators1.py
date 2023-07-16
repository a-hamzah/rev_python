import time

def tictoc(func):
    def wrapper():
        t1 = time.time() # current time
        func()
        t2 = time.time() - t1
        # print(f'took {t2} seconds')
        print(f'{func.__name__} ran in {t2} seconds')
    return wrapper

@tictoc
def his_name():
    # print("His name is Alan")
    time.sleep(1.1)

@tictoc
def his_address():
    # print("His address is Hauwai Island")
    time.sleep(0.3)

his_name()
his_address()
print('Done')

