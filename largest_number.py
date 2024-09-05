def find_largest_number(lst):
    largest=lst[0]
    print("test")
    for num in lst:
        if num>largest:
            largest=num
    return largest

lst=[300000,5,4,7,1,2,5,66,4,44,200,2123,4]
output=find_largest_number(lst)
print(f"{output} is largest number in given {lst} list")
