a="3792"
b="5342"
c="2372"
d=sorted(a[0]+b[0]+c[0])
e=sorted(a[1]+b[1]+c[1])
f=sorted(a[2]+b[2]+c[2])
g=sorted(a[3]+b[3]+c[3])
s=(d[0]+e[0]+f[0]+g[0])
print(s)
if int(s)>9:
    print(sum(map(int,str(s))))
