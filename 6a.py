filename=input("Enter filename:")
f1=open(filename)
N=int(input("Enter number of lines to be displayed:"))
word=input('Enter word to count its frequency of occurence in the file:')
linenumber=0
for line in f1:
    if linenumber==N:
        break
    print(line)
    linenumber=linenumber+1
f1=open(filename)
count=0
for line in f1:
    if word in line.split():
        count=count+1
print("Frequency of given word is ")
print(count)
