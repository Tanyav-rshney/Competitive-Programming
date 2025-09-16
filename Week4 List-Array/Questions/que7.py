# given a list of integers and a target no,find and print index of the target in the list.

arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target number: "))
for i in range(len(arr)):
    if arr[i] == target:
        print(i)       
        break
else:
    print("not found")          
