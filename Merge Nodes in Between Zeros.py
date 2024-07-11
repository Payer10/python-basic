l = list(map(int,input().split()))
new_l = []
v = l[0]
for i in range(1,len(l)):
    if l[i] == 0:
        new_l.append(v)
        v = 0
    else:
        v += l[i]
print(*new_l)

