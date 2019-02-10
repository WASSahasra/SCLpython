for x in range(1,3):
    n=str(input("Enter the Name:-  "))
    m=float(input("Enter the Marks:-  "))
    if m>=75:
        g="A"
    elif m>=60:
        g="B"
    elif m>=55:
        g="C"
    elif m>=40:
        g="S"
    else:
        g="F"
    print("Name of Student:-",n)
    print("Your Grade is:-",g)
    
