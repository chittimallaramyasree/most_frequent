print("enter no of elements")
n=int(input())
print(n)
l=[]
for i in range(0,n):
    ele=int(input())
    l.append(ele)
for i in l:
    if i>=0:
        print(i,end=" ")
    else:
        pass
