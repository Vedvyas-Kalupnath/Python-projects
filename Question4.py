# function definition for lcm
def lcm(num1, num2):


# comparison num1 with num2
   if num1 > num2:


#if num 1 > num 2, greater is assigned value of num 1
       greater = num1


   else:
#if num 1 not > num 2, greater is assigned value of num 2
       greater = num2


#infinite while loop checks:
# if greater modulo num 1 =0 and modulo num 2 = 0
# lcm is assigned value greater
#at break loop exits


   while(True):
       if((greater % num1 == 0) and (greater % num2 == 0)):
           lcm = greater
           break


# else loops runs and add 1 to greater until above condition is reached
       greater += 1


#returns lcm to function
   return lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))