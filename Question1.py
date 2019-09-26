#iniatialising some varaiables
ucase=0;
lcase=0;
digits=0;
specialchar=0;

#accepting input from user
sentence = input("Enter your sentence:")

#using for loop syntax with if staments
for search in sentence:
    if search.isupper():
        ucase+= 1
    elif search.islower():
     lcase+=1
    elif search.isdigit():
        digits+=1
    else:
        specialchar+=1

#displaying output
print("Number of uppercase characters is:", ucase)
print("Number of lowercase characters is:", lcase)
print("Number of digits is:", digits)
print("Number of special characters is:", specialchar)
