def bubble_sort(elements):
    n=len(elements)
    for i in range(n-1):
        for j in range(n-i-1):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
                

# def bubble_sort(elements):
#     n = len(elements)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if elements[j] > elements[j + 1]:
#                 elements[j]=elements[j + 1]
#                 elements[j + 1] = elements[j]

elements=[66,55,33,88,77,66,11,223,3,41,0,657565]
bubble_sort(elements)
print(elements)
