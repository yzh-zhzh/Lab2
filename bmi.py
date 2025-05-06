def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("Your BMI is:" + str(round(bmi, 2)))
    
    if bmi<18.5:
        return -1
    elif 18.5<=bmi<=25.0:
        return 0
    elif bmi>25.0:
        return 1

def main():
    calculate_bmi(weight=60, height=1.73)

if __name__ == '__main__':
    main()