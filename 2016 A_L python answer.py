price_due=0.0
IP=[10.00,12.00,10.00,15.00,25.00,45.00,50.00,25.00,10.00,12.00]
FT=int(input("Enter food type:"))
while FT!=0:
    IQ=int(input("Enter the Quntity:"))
    price_due=price_due+IP[FT-1]*IQ
    FT=int(input("Enter food type"))
print(price_due)
