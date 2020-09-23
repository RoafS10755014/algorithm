#selection sort
import random
arr = list(range(15))
random.shuffle(arr)
print(arr)

for i in range(len(arr)-1):
    index = i
    j = i+1
    selected = arr[i]
    while j<len(arr):
        if arr[j]<selected:
            selected = arr[j]
            index = j
        j=j+1
    arr[index],arr[i] = arr[i],arr[index]
print(arr)
    
        
        
