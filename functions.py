class BMI:
    def __init__(self) -> None:
        pass

    def greet(self):
        print('Welcome to BMI Calculator')

    def input(self):
        self.name = input('Name: ')
        self.weight = input('Enter your weight: ')
        print("Select Measurement ['kg', 'lbs']")
        self.weight_measurement = input('Weight Measurement: ')
        self.calculate_weight()

        self.height = input('Enter your height: ')
        print("Select Measurement ['inch', 'cm', 'm']")
        self.height_measurement = input('Height Measurement: ')
    
    def calculate_weight(self):
        if self.weight_measurement.lower() == 'lbs':
            self.final_weight = round((int(self.weight) * 0.454), 0)
            return self.final_weight
        elif self.weight_measurement.lower() == 'kg':
            self.final_weight = round(int(self.weight), 0)
            return self.final_weight
        else:
            return None
            
    def calculate_height(self):
        pass
        

    def calculate_bmi(self):
        pass

    