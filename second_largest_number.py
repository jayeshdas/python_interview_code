def find_second_largest_number(elements):
    largest=float()
    second_largest=float()
    for i in elements:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest>largest:
            second_largest=i

    return second_largest

lst=[33,2,2,8,2,5,9,56,6,7,7,7,66,8,0,211,23,4,1,66]
output=find_second_largest_number(lst)
print(output)