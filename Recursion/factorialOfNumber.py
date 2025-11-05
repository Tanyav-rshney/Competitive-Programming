#factorial of number
def fact(N):
    if N == 0: #base condition
        return 1
    else:
        return (fact(N-1) * N) #main logic
n=int(input())
print(fact(n))