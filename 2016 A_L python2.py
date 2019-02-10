n=int(input("Enter amount of food item: "))
c=1
t=0
while c<=n:
    x=int(input("Enter food code: "))
    if x>0 and x<=10:
        p=int(input("Enter unit price: "))
        q=int(input("Enter Quntity: "))
        t=t+p*q
    c=c+1
print("Net bill is: ",t)
