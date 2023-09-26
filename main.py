from functions import BMI

if __name__ == '__main__':
    calculator = BMI()
    calculator.greet()
    calculator.input()
    calculator.calculate_weight()
    calculator.calculate_height()
    bmi = calculator.calculate_bmi()
    print(bmi)
    calculator.classification(bmi)