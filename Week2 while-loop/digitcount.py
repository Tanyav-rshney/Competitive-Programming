#count digits of a number

n = int(input("Enter number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)