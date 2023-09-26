from conversion import Conversion

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
            self.final_weight = Conversion.convert_kgs(self.weight)
        elif self.weight_measurement.lower() == 'kg':
            self.final_weight = round(int(self.weight), 0)
            
    def calculate_height(self):
        if self.height_measurement.lower() == 'inch':
            self.final_height = Conversion.convert_inch(self.height)
        elif self.height_measurement.lower() == 'cm':
            self.final_height = Conversion.convert_cm(self.height)
        elif self.height_measurement.lower() == 'm':
            self.final_height = Conversion.convert_mtr(self.height)


    def calculate_bmi(self):
        BMI = self.final_weight / self.final_height
        return round(BMI, 2)
    
    def classification(self, BMI):
        if BMI <= 18.5:
            print(f"{self.name} you are 'Underweight'")
        elif BMI <= 24.9:
            print(f"{self.name} you are 'Normal Weight'")
        elif BMI <= 29.9:
            print(f"{self.name} you are 'Overweight'")
        elif BMI <= 34.9:
            print(f"{self.name} you are 'Class 1 Obese'")
        elif BMI <= 39.9:
            print(f"{self.name} you are 'Class 2 Obese'")
        else:
            print(f"{self.name} you are 'Class 3 Obese'")