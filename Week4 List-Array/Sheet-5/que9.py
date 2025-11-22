n=int(input())
l=list(map(int, input().split()))
Passed=0
Fail=0
for i in range(len(l)):
    if l[i] >= 35:
        Passed += 1
    else:
        Fail += 1
print(Passed,Fail)