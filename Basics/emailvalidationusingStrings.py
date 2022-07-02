email = input('Enter your email')
k = 0
j = 0
d = 0
if len(email)>6:
    if  email[0].isalpha():
        if ("@" in email) and (email.count('@')== 1):
            if (email[-4] == '.') ^ (email[-3] == '.'): # returns false it both are true and 
                #returns true if both are opposite
                for char in email:
                    if char.isspace():
                        j = 1

                    elif char.isalpha():
                        if char.isupper():
                            print('wrong email 6')

                    elif char.isdigit(): # continue the loop
                        continue
                    
                    elif char == '_' or char == '.' or char == '@':
                        continue
                    else:
                        d = 1

                if k == 1 and j == 1 or d == 1:
                    print('wrong email 5')

            else:
                print('wrong email 4')
        else:
            print('wrong email 3')
    else:
        print("wrong email2")
else:
    print('wrong email1 ')