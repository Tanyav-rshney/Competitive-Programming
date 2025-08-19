#Divisible by 3 and last digit is 4

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 10 == 4:
    print("divisible by 3 and last digit is 4")
else:
    print("no")

