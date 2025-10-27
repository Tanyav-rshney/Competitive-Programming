a=input()
new=a+a
result=" "
for i in new:
    if i==i.lower():
        if i in 'aeiou':
            result+="#"
        else:
            result+=i
print(result)


