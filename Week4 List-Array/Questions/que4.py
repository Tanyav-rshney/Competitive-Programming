# given an array and increment number generate a new array which contains all values of original array increased by increment value.

arr = list(map(int, input().split()))
inc = int(input("Enter inc value: "))

for i in range(len(arr)):
    arr[i] += inc  
print(arr)