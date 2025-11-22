def count(n):
    if n<0:
        n=-n
    if n==0:
        return 0
    return 1 + count(n//10)
n = int(input())
if n==0:
    print(1)
else:
    print(count(n))