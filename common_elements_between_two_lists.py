def check_comman_element(lst1,lst2):
    comman=[]
    for i in lst1:
        if i in lst2:
            comman.append(i)

    return comman


lst1=[4,3,3,3,2,222,5,5,6,6,6,74,76,322,5,4,4,4,4]
lst2=[2,123,234,545]

output=check_comman_element(lst1,lst2)
print(output)
