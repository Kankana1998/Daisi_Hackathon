import sys

 # sys.stdin to read from stdinput
for number in sys.stdin:
    #first strip the phone numbers
    given_ph_number = number.strip()
    #store the first 3 digits as area code
    area_code = given_ph_number[0:3]
    #store the next three digits as first three digits
    next_num = given_ph_number[3:6]
    #atlast store the last part from 6 to up until the last digit
    last_num   = given_ph_number[6:]
    #at last print the phone number in the transformed form
    print("(%s) %s-%s" % (area_code, next_num, last_num))