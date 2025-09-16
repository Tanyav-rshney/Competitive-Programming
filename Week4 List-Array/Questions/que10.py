n = int(input())
l = list(map(int, input().split()))
result = []

for i in range(len(l)):
    if l[i] % 2 == 0:
        result.append(l[i])   

if result:
    print(result)
else:
    print("-1")
