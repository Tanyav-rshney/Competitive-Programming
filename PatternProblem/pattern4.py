# n = int(input("Enter the value of n: "))

# # Upper half
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         print("*", end="")
#     for j in range(2*i-2):
#         print(" ", end="")
#     for j in range(n-i+1):
#         print("*", end="")
#     print()

# # Lower half
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     for j in range(2*n-2*i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


n = int(input("Enter the value of n: "))

for i in range(1, 2*n + 1):
    if i <= n:
        stars = n - i + 1
        spaces = 2 * (i - 1)
    else:
        stars = i - n
        spaces = 2 * (2*n - i)
    
    print("*" * stars + " " * spaces + "*" * stars)

