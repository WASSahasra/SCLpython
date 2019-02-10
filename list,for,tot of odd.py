oddnum=[]
for x in range (10):
    y=int(input("Enter Num "))
    if y%2==1:
        oddnum.append(y)
t=0
for z in range (len(oddnum)):
    t=t+oddnum[z]
print(oddnum)
print("Total is ",t)
