#Sum of all natural numbers from 1 to N by for loop

n=int(input())
i=1
total=0
for i in range(1,n+1):
    total += i
print(total)
    

# sum of natural number by recursion
def Sum(N):
    if N == 1: #base case
        return 1
    else:
        return (Sum(N-1)+N) # main logic
n=int(input())
print(Sum(n))


