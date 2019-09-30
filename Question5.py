# function definition for hcf
def hcf(num1, num2):

# comparison num1 with num2
    if num1 > num2:

# if num 1 > num 2, smaller is assigned value of num 2
        smaller = num2

#if num 1 not > num 2, smaller is assigned value of num 1
    else:
        smaller = num1

#range check:
# if num modulo i =0 and num 2 modulo = 0
# hcf is assigned value i


    for i in range(1, smaller + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            hcf = i

# returns hcf to function
    return hcf


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The H.C.F. of", num1, "and", num2, "is", hcf(num1, num2))