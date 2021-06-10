age = int(input("input your age"))

gender = input("Input your gender : ")
while gender not in ['male', 'female']:
    print("Please re-enter your gender")
    gender = input("Input your gender : ")

weight = float(input("Input your weight in kg"))
height = float(input("input your height in M"))

# formula for calculating bmi
bmi = (weight /(height*height))

if gender == 'male':
    print("Sir your BMI is:",round (bmi, 2))

elif gender == 'female':
        print("Madam your BMI is:",round(bmi,2))

else :
        print(gender)
