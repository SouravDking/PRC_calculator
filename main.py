def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("welcome to calculator app")
print("select options from 1,2,3,4")
print("1. addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

while True:
    choice = input("enter choice(1/2/3/4):")

    if choice in ('1','2','3','4'):
        num1 = float(input('first number:'))
        num2 = float(input('2nd number:'))

        if choice == '1':
            print (num1 , '+' , num2 ,'=', add(num1,num2))

        elif choice == '2':
            print (num1 , '-' , num2 ,'=', sub(num1,num2))

        elif choice == '3':
            print (num1 , '*' , num2 ,'=', mul(num1,num2))
        
        elif choice == '1':
            print (num1 , '/' , num2 ,'=', div(num1,num2))
        break
    else:
        print("invalid input")