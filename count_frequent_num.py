def find_frequent_number(lst):
    print(lst)
    frequent={}
    for i in lst:
        if i in frequent:
            frequent[i]+=1
        else:
            frequent[i]=1
    return frequent


lst=[3,5,4,3,33,4,55,7,8,7,65,4,3,3,22,2]
output=find_frequent_number(lst)
print(output)
