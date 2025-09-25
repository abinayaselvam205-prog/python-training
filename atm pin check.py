print("welcome to our ATM")
pin="638264"
while True:
    start=input("enter ATM pin:")
    if start==pin:
        print("pin accepted,access granted")
        a=int(input("enter the amount:"))
        print(" collect the card!! and wait for amount")
        break
    else:
        print("invalid pin.please try again!!")
        