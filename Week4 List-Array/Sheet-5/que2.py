# given an array find max value in it

arr = list(map(int, input().split()))
# max= arr[0]
# for i in range (len(arr)):
#     if arr[i] > max:
#         max = arr[i]

# print( max)

#function to find max
ans= -float("inf") 
for i in arr:
     if (ans<i):
        ans = i
print(ans)
