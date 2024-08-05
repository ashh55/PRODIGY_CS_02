import re

password = input('Enter Password : ')

check = 0

if  re.search("\s",password):
    check = check + 10
if (len(password)<=7):
    check = check + 1
if not re.search("[a-z]",password):
    check = check + 1
if not re.search("[A-Z]",password):
    check =  check + 1
if not re.search("[0-9]",password):
    check =  check + 1
if not re.search("[_@$]",password):
    check = check + 1
if not re.search("[_@$]",password):
    check = check + 1

if (check >=10):
    print('Invalid Password')
elif (check == 0 ):
    print('Very Strong Password')
elif (check == 1):
    print('Strong Password')
elif (check == 2):
    print('Medium Password')
elif (check == 3):
    print('Medium Password')
elif (check == 4):
    print('Weak Password')
elif (check == 6 or check == 5):
    print('Very Weak Password')