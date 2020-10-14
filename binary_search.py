def binarySearch(arr, l, r, x):
    #print(r, l)
    if r>=l:
        mid = l+(r-l)// 2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

def bubble_sort(arr):
    for i in range(len(arr)):
        j=0
        while j<len(arr)-1-i:
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
            j = j+1
    return arr

numArr=[]
while(True):
    value = input("please enter a number\n")
    if value.isdigit():
        value = int(value)
        numArr.append(value)
        if len(numArr) >= 5: break
    else:
        print("invalid input...")

if len(numArr) != 0:
    print("before: ", numArr)
    numArr = bubble_sort(numArr)
    print("after: ", numArr)

    while(True):
        target = input("enter the value you want to find\n")
        if target.isdigit():
            target = int(target)
            result = binarySearch(numArr, 0, len(numArr)-1, target)
            if result != -1:
                print("element inputted is at index ", result, "\n")
            else:
                print("cannot found element in the array\n")
        else:
            print("invalid input...")



'''
arr=[5,8,9,15,30]
x = 0
#function call

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print(" element is at index ", result)
else:
    print("cannot found element in the array")
    '''

