num=int(input('Enter an integer:'))
power=len(str(num))
sum=0
temp=num
while temp>0:
    rem=temp%10
    sum=sum+rem**power
    temp//=10
if num==sum:
    print(num,"is a Armstrong number")
else:
    print(num,"is not a Armstrong number")
        
              
