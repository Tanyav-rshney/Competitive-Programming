#Triangle type (Right, Obtuse, Acute)

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Not a valid triangle")
else:
    if a == 90 or b == 90 or c == 90:
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
