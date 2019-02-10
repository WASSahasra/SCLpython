'''c=1
tot=0
while c<=10:
    x=int(input("Enter num:- "))
    tot=tot+x
    c=c+1
print(tot)'''
def totNum (x,y):
    tot=x+y
    return(tot)
'''c=1
tot=0
while c<=10:
    x=int(input("Enter num:- "))
    tot=tot+x
    c=c+1
print(tot)'''
t=0
for c in range (10):
    x=int (input("Enter num:- "))
    t=totNum(t,x)
print(t)

