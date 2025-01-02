class Celsius:
    def __init__(self, temperature = 0) -> None:
        self.temperature = temperature
        self.temperature_history = []

    def __str__(self):
        return f'\nTemperature = {self.temperature}\n'
    
    def set_temperature(self, celsius_temperature):
        self.temperature = celsius_temperature
        self.temperature_history.append(celsius_temperature)
    
    def to_farhenheit(self):
        return (self.temperature * 1.8) + 32
    
    def status(self):
        if self.temperature <= 20:
            print(f'Set temperature {self.temperature} is LOW')
        else:
            print(f'Set temperature {self.temperature} is HIGH')

    def print_history(self):
        for thermostate in self.temperature_history:
            print(thermostate)


obj = Celsius()
print(obj)
obj.status()
print(obj.to_farhenheit())
obj.set_temperature(30)
obj.status()
print(obj.to_farhenheit())

obj.set_temperature(15)
obj.status()

obj.print_history()