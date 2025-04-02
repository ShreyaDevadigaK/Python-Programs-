class PaliStr:
    def __init__(self):
        self.isPali=False

    def chkpalindrome(self,mystr):
        if mystr==mystr[::-1]:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali

class PaliInt(PaliStr):
    def __init__(self):
        self.isPali=False
    def  chkpalindrome(self,val):
        temp=val
        rev=0
        while temp!=0:
          dig=temp%10
          rev=(rev*10)+dig
          temp=temp//10
        if val==rev:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali

st=input('Enter a string:')
stObj=PaliStr()
if stObj.chkpalindrome(st):
    print('Given string is Palindrome')
else:
    print('Given string is not a Palindrome')

val=int(input('Enter an integer:'))
intObj=PaliInt()
if intObj.chkpalindrome(val):
    print('Given integer is Palindrome')
else:
    print('Given integer is not a Palindrome')
