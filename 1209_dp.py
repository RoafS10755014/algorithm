#Rod cutting problem

maxValue = []
def getmax(rod, n): #rod:長度價格對應表, n:長度
    if n<=1:
        return rod[n]
    else:
        for i in range(n):
            maxValue.append(getvalue(rod, i, n))
        return max(maxValue)

def getvalue(rod, n, maxvalue):
    return rod[n] + rod[maxvalue-n]


ROD = [0,1,5,8,9,10,17,17,20,24,30]

userinput = input("please input a number\n")
while True:
    if userinput.isdigit():
        userinput = int(userinput)
        if userinput>10:
            userinput = input("please enter a number(0~10)")
        else:
            break
    else:
        userinput = input("please input a number\n")
print(getmax(ROD, userinput))
#print(rod)
