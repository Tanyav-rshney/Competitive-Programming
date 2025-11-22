# *        *
# **      **
# ***    ***
# ****  ****
# **********

# n=int(input())
# for i in range (n,0,-1):
#     for j in range(n-i+1):
#         print("*", end="")
#     for j in range(2*i-2):
#         print(" ", end="")
#     for j in range(n-i+1):
#         print("*", end="")
#     print()

n=int(input())
for i in range (1,n+1):
    for j in range(i):
        print("*", end="")
    for j in range(2*n-2*i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()