arr=[25,11,7,75,89]
min=arr[0]
for i in range (0,len (arr)):
    if(arr[i]<min):
        min=arr[i]

print("The given array is :",arr)
print('Minimum value present in given list:'+str(min))
