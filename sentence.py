str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0
digits = 0

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    elif (i == '0' or i == '1' or i == '2' or i == '3' or i == '4'
            or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
        digits = digits + 1
    else:
        consonants = consonants + 1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
print("Total Number of digits in this String = ", digits)