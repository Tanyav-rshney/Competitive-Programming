#using recursion print no from 1 to n
def num(n):
    if n == 0:
        return
    num(n-1)   
    print(n)         

n = int(input())
num(n)


#print the no from n to 1
def num(n):
    if n == 0:
        return
    print(n) 
    num(n-1)        

n = int(input())
num(n)







