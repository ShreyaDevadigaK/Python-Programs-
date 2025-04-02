import re
def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

def chkPhonenumber (numstr):
    ph_no_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match (numstr):
        return True
    else:
        return False

print("Without using Regular Expression")
print("Is 415-555-4242 a phone number ?")
print(isPhoneNumber('415-555-4242'))
print('Is user a phone number ?')
print(isPhoneNumber('user'))
print("With using Regular Expression")
print("Is 415-555-4242 a phone number ?")
print(chkPhonenumber('415-555-4242'))
print("Is 415-555-42434 a phone number ?")
print(chkPhonenumber('415-555-42434'))
