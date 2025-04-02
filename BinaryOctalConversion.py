def BintoDec(num):
    dnum=0
    i=1
    while num!=0:
        rem=num%10
        dnum=dnum+(rem*i)
        i=i*2
        num=int(num/10)
    return dnum

binum=int(input("Enter a Binary number:"))
decinum=BintoDec(binum)
print("The Equivalent decimal number is:",decinum)

def OcttoDec(num):
    decimal = 0
    power = 0
    while num!= 0:
        last_digit = num % 10
        decimal += last_digit * (8 ** power)
        num //= 10
        power += 1
    return decimal

def DecitoHexa(decimal):
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal != 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder]+ hexadecimal 
        decimal //= 16
    return hexadecimal

octnum = int(input("Enter an octal number: "))
decimal_number = OcttoDec(octnum)
hexadecimal_number = DecitoHexa(decimal_number)

print("Hexadecimal equivalent:",hexadecimal_number)
