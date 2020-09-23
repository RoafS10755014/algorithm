#insert sort
import random
arr = list(range(15))
random.shuffle(arr)
print(arr)


for i in range(len(arr)-1):
    j = i
    while j >= 0:
        if arr[j] >= arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
        j = j-1
print(arr)

