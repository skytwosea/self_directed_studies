start = 0
poles = [[],[],[]]
n = 3
m = n-1
c = 97
l = len(poles)
for k in range(l):
    while m >= 0:
        poles[k].append(chr(m+c))
        m -= 1
    m = n-1
    c += n

rpoles = [*zip(*poles)][::-1]

for j in range(l):
    print(rpoles[j])
