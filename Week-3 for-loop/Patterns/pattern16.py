# * * * * * 
# _ * * * * 
# _ _ * * * 
# _ _ _ * * 
# _ _ _ _ * 

n=int(input())
for i in range (n,0,-1):
    for j in range(n-i):
        print("_", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()