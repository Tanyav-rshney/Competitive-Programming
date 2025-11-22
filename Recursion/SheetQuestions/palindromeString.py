#Check if a string is a palindrome 

def palin(s):
    if len(s)<2:
        return True
    if s[0] != s[-1]:
        return False
    return palin(s[1:-1])
s=input()
if palin(s):
    print("palindrome")
else:
    print("not palindrome")