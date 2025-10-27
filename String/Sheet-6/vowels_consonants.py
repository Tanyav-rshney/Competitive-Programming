t=int(input())
for i in range(t):


    a=input()
    vowels=0
    conso=0

    for ch in a.lower():
        if ch in "aeiou":
            vowels+=1
        elif ch.isalpha():
            conso+=1

    print(vowels,conso)