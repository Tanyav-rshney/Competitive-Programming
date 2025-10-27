a=input()
# char="e"
# count=0
# for i in a:
#     if i==char:
#         count+=1
# print(count)

count=0
# for i in range(len(a)):
#     if a[i:i+3]=="bob":
#         count+=1
# print(count)
# b=a.count("bob")
# print(b)

for i in range(len(a)):
    if(a[i]=='b') and a[i+1]=='o' and a[i+2]=='b':
        count+=1
print(count)