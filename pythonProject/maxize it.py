from itertools import product
k,m = list(map(int,input().split()))

l = []
for i in range(k):
    a = list(map(int,input().split()))
    l.append(a[1:])

mylist = []

y = list(product(*l))

for d in range(len(y)):
    s = 0
    for j in y[d]:
        s = (j**2 + s)
    mylist.append(s%m)

mx = max(mylist)
print(mx)

