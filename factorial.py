def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

num=52 
output=factorial(num)
print(f"factorial of {num} is {output}")
