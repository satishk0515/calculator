import time
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def pow(x,y):
    return x**y

print("select the operations:")
print("1.addition")
print("2.subtration")
print("3.multiplication")
print("4.division")
print("5.power")

while True:
    choice=input("select the operations (1,2,3,4,5):")
    if choice in ('1','2','3','4','5',):
        try:
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
        except ValueError:
            print("invalid input. please enter the number.")
            continue
        if choice=='1':
            print(num1, "+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1, "-",num2,"=",sub(num1,num2))
        elif choice=='3':
            print(num1, "*",num2,"=",mul(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",div(num1,num2))
        elif choice=='5':
            print(num1,"^",num2,"=",pow(num1,num2))
        nex_calculator=input("let's do next calculation?(yes/no):")
        if nex_calculator == "no":
            break
    else:
        print("invalid input")






