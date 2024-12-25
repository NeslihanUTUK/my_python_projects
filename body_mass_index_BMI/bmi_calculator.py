# BMI Calculator Script

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = float(weight / height ** 2)
print("Your Body Mass Index (BMI) is: ", bmi)

if bmi < 25:
    print("You are underweight.")
elif 25 <= bmi < 30:
    print("You have a normal weight.")
elif 30 <= bmi <= 40:
    print("You are overweight.")
else:
    print("You are obese.")
