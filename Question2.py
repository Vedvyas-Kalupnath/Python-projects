# using basic knowledge since there are only four lists and it is easier for everyone to understand
# creating four empty lists

list1 = []
list2 = []
list3 = []
list4 = []

#accepting inputs and assigning to variables
print("Please enter numbers for list1,list2,list3,list4 respectively.")
print(" ")
num1 = int(input('1st no. list1:'))
num2 = int(input('2nd no. list1:'))
num3 = int(input('3rd no. list1:'))
num4 = int(input('4th no. list1:'))

#adding each user input(numbers) at end of list
list1.append(num1)
list1.append(num2)
list1.append(num3)
list1.append(num4)

print("___________________________")
num1 = int(input('1st no. list2:'))
num2 = int(input('2nd no. list2:'))
num3 = int(input('3rd no. list2:'))
num4 = int(input('4th no. list2:'))

list2.append(num1)
list2.append(num2)
list2.append(num3)
list2.append(num4)

print("___________________________")
num1 = int(input('1st no. list3:'))
num2 = int(input('2nd no. list3:'))
num3 = int(input('3rd no. list3:'))
num4 = int(input('4th no. list3:'))

list3.append(num1)
list3.append(num2)
list3.append(num3)
list3.append(num4)

print("___________________________")
num1 = int(input('1st no. list4:'))
num2 = int(input('2nd no. list4:'))
num3 = int(input('3rd no. list4:'))
num4 = int(input('4th no. list4:'))

list4.append(num1)
list4.append(num2)
list4.append(num3)
list4.append(num4)

print("___________________________")
print("List 1 is:",list1)
print("List 2 is:",list2)
print("List 3 is:",list3)
print("List 4 is:",list4)

print("___________________________")

#adding all elements in respective lists
sum1 = 0
for num1 in list1:
     sum1 += int (num1)


sum2 = 0
for num2 in list2:
     sum2 += int (num2)


sum3 = 0
for num3 in list3:
     sum3 += int (num3)


sum4 = 0
for num4 in list4:
     sum4 += int (num4)

# if statements for sum comparison; finding highest sum
if (sum1 > sum2) and (sum1 > sum3) and (sum1 > sum4):
    largest = sum1
    print("The list with highest sum of elements is:",list1)

elif (sum2 > sum1) and (sum2 > sum3) and (sum2 > sum4):
    largest = sum2
    print("The list with highest sum of elements is:", list2)

elif (sum3 > sum1) and (sum3 > sum2) and (sum3 > sum4):
    largest = sum3
    print("The list with highest sum of elements is:", list3)

else:
    largest = sum4

#displaying list with highest sum of elements
    print("The list with highest sum of elements is:", list4)




