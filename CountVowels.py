str = "User"
count = 0
vowel = set("aeiouAEIOU")
print("String :",str)
print("Vowels :",vowel)
for alphabet in str:
    if alphabet in vowel:
        count = count + 1
print("Number of Vowels :", count)
