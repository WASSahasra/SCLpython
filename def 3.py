'''a=int(input("Enter num:- "))
f=1
for c in range (a,0,-1):
    print(c)
    f=f*c
print(f)'''
def fNum (a):
    f=1
    for c in range(a,0,-1):
        print(c)
        f=f*c
    return (f)
x=int(input("Enter num:- "))
print(fNum(x))

