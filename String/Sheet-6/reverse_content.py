a=input()
b=a.split()
l1=[]
for word in b:
    l1.append(word[::-1])
result=" ".join(l1)
print(result)
