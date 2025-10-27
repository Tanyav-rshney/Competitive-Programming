a=input()
b=int(input())
char=chr(b)
found=0

for  i in range(len(a)):
    if a[i]==char:
        found=i
        break

print(found)