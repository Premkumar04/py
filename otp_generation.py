a=input()
b=input()
c=int(b)
while c>9:
    c=sum(map(int,str(c)))  
print(b[0],end="")
print(a[0].swapcase(),end="")
print(c,end="")
print(a[-1],end="")
