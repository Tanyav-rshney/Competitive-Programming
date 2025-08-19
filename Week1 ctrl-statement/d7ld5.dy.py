#Divisible by 7 or last digit is 5

num = int(input("Enter a number: "))
if num % 7 == 0 or num % 10 == 5:
    print("Yes")
else:
    print("No")
