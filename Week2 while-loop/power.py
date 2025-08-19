# Find A^B (Power)


A = int(input("Enter A: "))
B = int(input("Enter B: "))
result = 1
i = 1
while i <= B:
    result *= A
    i += 1
print(result)