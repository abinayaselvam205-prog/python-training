def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return"error:divison by zero"
    return a/b
print("=====simple calculator=====")
while True:
    print("choose option:")
    print("1.Add(+)")
    print("2.Sub(-)")
    print("3.mul(*)")
    print("4.div(/)")
    op=(input("enter your choice(+,-,*,/):"))
    x=float(input("enter the first number:"))
    y=float(input("enter the second number:"))
    if(op=='+'):
        print("result=",x+y)
    elif(op=='-'):
        print("result=",x-y)
    elif(op=='*'):
        print("result=",x*y)
    elif(op=='/'):
        print("result=",x/y)
    else:
        print("invalid")
    
