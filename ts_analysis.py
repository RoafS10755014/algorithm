#判斷某個月是否為31天

year = {1:31, 2:28, 3:31, 4:30, 5:31,
        6:30, 7:31, 8:31, 9:30, 10:31,
        11:30, 12:31}

#time complecity
def timedetect(month):
    if(year[month])==31:
        return True
    else:
        return False

#space complecity
def spacedetect(month):
    days31 = [1, 3, 5, 7, 8, 10, 12]
    if(month in days31):
        return True
    else:
        return False

print("detect every month if it has 31 days")
for i in range(12):
    i+=1;
    print("time:", i, "is ", end="");print(timedetect(i))
    print("spece", i, "is ", end="");print(spacedetect(i))
#output photo is at 2020/10/02 assignment
