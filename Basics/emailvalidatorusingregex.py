"""
a-z,
0-9, 
. _ should not be more than one,
@ should be only one ,
. should be in 2nd or 3rd position from the end

"""
import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
#\ is used for searching in regex
# ? returns is there is more than 1 
# \w for searching
# curly brackets for custom searching
# $ for searching from back
user_email = input("Enter your email:\n")

if re.search(email_condition, user_email):
    print("Right email")
else:
    print('Wrong email')