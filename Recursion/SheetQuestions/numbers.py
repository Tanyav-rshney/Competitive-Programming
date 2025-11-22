#using recursion print numbers from 1 to n.
# print the numbers from n to 1.

# print the numbers from n to 1.
def num(n):
    if n==0:
        return
    print(n)
    num(n-1)
n = int(input())
num(n)

#using recursion print numbers from 1 to n.
def num(n):
    if n==0:
        return
    num(n-1)
    print(n)
n = int(input())
num(n)