terms=int(input("enter the terms:"))
a=1
b=0
count=0
print("fibonacci series")
while(count<=terms):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    count=count+1