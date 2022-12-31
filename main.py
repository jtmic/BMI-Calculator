
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = int(weight) / float(height) ** 2
bmi_as_float = float(bmi)
bmi_as_int = int(bmi)

if bmi_as_float < 18.5: 
    print(f"your bmi is {bmi_as_float}, you are underweight.")

elif bmi_as_int < 25: 
    print(f"your bmi is {bmi_as_float}, you have a normal weight.")

elif bmi_as_int < 30: 
    print(f"your bmi is {bmi_as_float} you are slightly overweight")

elif bmi_as_int  < 35: 
    print(f"your bmi is {bmi_as_float} you are obese")

elif bmi_as_int > 35: 
    print(f"your bmi is {bmi_as_float} you are clinically obese")
    
else: print("you are underweight.")

