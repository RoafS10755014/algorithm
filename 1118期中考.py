#selection sort
import random

def selectionSort(arr):         #定義函式selection sort
    for i in range(len(arr)-1): 
        j = i+1                               #每次+1避免動到已經排序過的資料
        selected = arr[i]               #selection 會每次取出最小的 並讓那筆資料變成已排序
        index = i                            #selcted的資料index
        while j<len(arr):               #從接著未排序的所有資料中找出最小值
            if arr[j]<selected:         #只要資料比selected小就把那筆資料指派給selected
                selected = arr[j]       #資料值指派給selected
                index = j                    #將這筆資料index指派給selected
            j=j+1                                                   #往下一筆
        print('第%d次: ' %(i),end="")
        print(arr)
        arr[index],arr[i] = arr[i],arr[index]   #交換資料，將最小值指派到未排序的第一筆index
    return arr

#insertion sort
def insertionSort(arr):                                 #定義insertion sort
    for i in range(len(arr)-1):  
        j = i                                                           # 將j指派成i的值，避免影響到已排序的資料
        while j >= 0:                                          #此迴圈會將第i筆資料排到正確位置，排序結束後即為已排序資料
            if arr[j] <= arr[j+1]:                          #如果下一筆資料比當前資料小
                arr[j],arr[j+1] = arr[j+1], arr[j]   #置換兩筆資料的位置
            j = j-1                                                  #繼續往前一筆對比直到陣列最開始
        print('第%d次: ' %(i),end="")
        print(arr)
    return arr

array = list(range(8))
random.shuffle(array)
print("insetion sort:\n原始陣列: " , end="")
print(array)
array = selectionSort(array)
print("selection sort 最終排序結果：")
print(array)

for i in range(2): print()

array = list(range(8))
random.shuffle(array)
print("selection sort:\n原始陣列: " , end="")
print(array)
array = insertionSort(array)
print("insertion sort 最終排序結果：")
print(array)
    
