lenght=int(input("enter the length of the list:"))
lst=[]
for i in range(length):
    element=int(input("enter element"))
    lst.append(element)
print(lst)
count,cnt=0,0
for i in lst:
    if i%2==0:
        count+=1
    if i%2!=0:
        cnt+=1
print("total even numbers are:",count)
print("total odd numbers are:",cnt)