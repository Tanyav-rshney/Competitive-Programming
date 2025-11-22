# given an array compute the sum of all elements


l = list(map(int, input("Enter numbers: ").split()))

sum = 0
for i in range(len(l)):
    sum += l[i]

print("Sum:", sum)
