#bubble sort
import random

arr = list(range(15))
random.shuffle(arr)
print(arr)

for i in range(len(arr)):
    j=0
    while j<len(arr)-1-i:
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
        j = j+1
print(arr)
