def most_frequent(text):
    result={}
    for x in text:
        if x not in result:
            result[x]=0
        result[x]+=1
    sort_result=sorted(result.items(),key=lambda x: x[1],reverse=True)
    for i in sort_result:
        print(i[0]+":"+str(i[1]))
print("Please enter a string")
mystr=input()
most_frequent(mystr)


    
