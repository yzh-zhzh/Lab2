def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("Your BMI is:" + str(round(bmi, 2)))
    
    if bmi<18.5:
        print("Your BMI is classified as Under Weight.")
    elif 18.5<=bmi<=25.0:
        print("Your BMI is classified as Normal Weight.")
    elif bmi>25.0:
        print("Your BMI is classified as Over Weight.")

calculate_bmi(weight=57, height=1.73)