
#! Import String to create a list a to z and A TO Z in python

""" import string
char = []
for i in string.ascii_lowercase:
    char.append(i)

for j in string.ascii_uppercase:
    char.append(j)

print(char) """

# ! end of a code

#! Start of a Code to generate a password ##

import random 

password_list = []
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sym = ['!', '@', '#', '$','%', '&', '(', ')', '+', '=']

# * Letter count input 
print("How many charcter you want in your passsword : ")
char_len = int(input(""))

#* Symbol count input
print("How many symbol you want in your passsword : ")
symbol_len = int(input(""))

#* Number input count
print("How many number you want in your passsword : ")
number_len = int(input(""))

#* random pick charcter
for i in range(1, char_len +1):
    password_list += random.choice(char)

#* Random pick Symbol
for i in range(1, symbol_len +1):
    password_list += random.choice(sym)

#* Random pick number 
for i in range(1, number_len +1):
    password_list += random.choice(num)

#* password list shuffle to save from hacker
random.shuffle(password_list)

#* add a password variable
password = ""

#* add shuffled list into a string
for i in password_list:
    password += i

print("Generated Pass word: ", password)


#! End of a code to generate pasword
