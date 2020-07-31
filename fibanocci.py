print("enter value n")
n=int(input())
a=0
b=1
if n<0:
    print("invalid")
elif n==1:
    print(a)
elif n==2:
    print(a,end=" ")
    print(b,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
