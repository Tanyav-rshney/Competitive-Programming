# given an array and  generate a new array which contains square of all no.

arr = list(map(int, input().split()))


for i in range(len(arr)):
    arr[i] = arr[i] ** 2
print(arr)