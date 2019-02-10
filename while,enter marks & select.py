c=1
t=0
while c<=10:
    x=str(input("Enter the Name:- "))
    y=float(input("Enter the Mark 1:- "))
    z=float(input("Enter the Mark 2:- "))
    a=(y+z)/2
    if a>=50:
        print((x),"You Are Selected")
    else:
        print((x),"You Are Not Selected")
    c=c+1
