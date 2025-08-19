#wap to input three numbers and print minimum among them

# num1=int(input("enter first no:"))
# num2=int(input("enter second no:"))
# num3=int(input("enter third no:"))

# minimum=min(num1,num2,num3)

# print("the minimum no. is:",minimum)


A = int(input("Enter number 1: "))
B = int(input("Enter number 2: "))
C = int(input("Enter number 3: "))

if A <= B and A <= C:
    print("Minimum is", A)
elif B <= A and B <= C:
    print("Minimum is", B)
else:
    print("Minimum is", C)

