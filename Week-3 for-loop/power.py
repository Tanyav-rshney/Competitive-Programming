# Power program using for loop

a = int(input("enter base number: "))
b = int(input("enter exponent: "))

result = 1

for i in range(b):
    result = result * a 

print(result)