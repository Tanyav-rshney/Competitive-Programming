#accept the percentage from the user display the grade

percentage = float(input("Enter your percentage: "))

if percentage < 25:
    print("Grade: D")
elif percentage < 45:
    print("Grade: C")
elif percentage < 65:
    print("Grade: B")
elif percentage < 85:
    print("Grade: A")
else:
    print("Grade: A+")
