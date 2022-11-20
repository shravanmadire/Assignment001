term=int(input("enter the last term till where you need fibonacci series"))
num1,num2=0,1
print("fibonacci series:",end=" ")
while num2<term:
    num3=num1+num2
    num1=num2
    num2=num3
    print(num1,end=" ")
