H =float(input("Please Enter your Hight ="))
W= float(input("Please Enter your Weight ="))
BMI = W/((H/100)**2)
if BMI < 18:
    print("you under weight")
elif BMI > 18 and BMI  < 25:
    print("you are Healthy")
else:
    print("you are over weight")
