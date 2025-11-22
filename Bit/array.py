# given an array of n integer where all the no. occurs even no of times except 1 which occurs odd no. of times, find that no.
#-> first line of the input contains integer n denoting the size of the array.
#-> next line of input contains n space contained spacing integers denoting the element of the array

n=int(input())
arr=list(map(int, input().split()))
ans=0
for i in arr:
    ans = ans^i
print(ans)