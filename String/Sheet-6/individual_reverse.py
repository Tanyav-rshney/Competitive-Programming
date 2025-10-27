s = input()
word=s.split()

for w in word:
    rev = ''
    for i in range(len(w) -1, -1, -1):
        rev += w[i]
    print(rev, end=' ')
