#Sum of all even numbers from 1 to A

A=int(input("enter n:"))
i=2
total=0
while i <= A:
    total += i
    i += 2
print(total)