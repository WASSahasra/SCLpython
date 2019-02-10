iN=int(input("Enter Index Num: "))
while iN!=0 or iN>0:
    sN=input("Enter Student name: ")
    print("Student name is: ",sN)
    hN=iN%3
    if hN>1:
        print("Your house is: Wijaya")
    elif hN>0:
        print("Your house is: Gemunu")
    else:
        print("Your house is: Thissa")
    iN=int(input("Enter Index Num: "))
