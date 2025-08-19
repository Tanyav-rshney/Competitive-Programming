#  Check if a number is palindrome

n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if rev == temp:
    print("Yes")
else:
    print("No")