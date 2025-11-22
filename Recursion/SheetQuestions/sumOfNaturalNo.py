merko#sum of n natural numbers


def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1) + n
n=int(input())
print(sum(n))

