price=[10,12,15,10,25,45,50,25,10,12]
i=True
t=0
while i==True:
    f=int(input("Enter Food Code:-"))
    if f>0 and f<=10:
        q=int(input("Enter Quntity:-"))
        p=price[f-1]
        t=t+p*q
    else:
        i=False
print("Net bill amount is",t)

