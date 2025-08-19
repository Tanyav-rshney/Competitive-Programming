#Sum of all odd numbers from 1 to A

A=int(input("enter n:"))
i=1
total=0
while i <= A:
    total += i
    i += 2
print(total)