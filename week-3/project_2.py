staff_name = input("Please enter your staff name: ")
staff_experience = input("Please enter your staff years of experience: ")
staff_age = input("Please enter your staff age: ")

if staff_experience > "25" and staff_age >= "55" :
    print(f"{staff_name} your Annual Tax Revenue(ATR) = 5,600,000")

elif staff_experience > "20" and staff_age >= "45" :
    print(f"{staff_name} your Annual Tax Revenue(ATR) = 4,480,000")
elif staff_experience > "10" and staff_age >= "35" :
    print(f"{staff_name} your Annual Tax Revenue(ATR) = 1,500,000")
else:
    print(f"{staff_name} your Annual Tax Revenue(ATR) = 550,000")
