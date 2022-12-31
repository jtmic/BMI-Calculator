height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



bmi = int(weight) / float(height) ** 2
bmi_as_float = float(bmi)
bmi_as_int = int(bmi)

if bmi_as_float < 18.5: print("you are underweight.")

elif bmi_as_int < 25 > 18.5: print("you have normal weight.") 

elif bmi_as_int > 25 > 35: print("you are slightly overweight")

elif bmi_as_int > 30 <+ 35: print("they are obese")

elif bmi_as_int > 35: print("you are clinically obese")
    
else: print("you are underweight.")

