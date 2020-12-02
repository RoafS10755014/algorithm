#零錢問題 貪婪法
#t = 面額
t = [25, 20, 5, 1]

#n = 總零錢
def change(t, n):
    m = [0 for _ in range(len(t))]
    for i , money in enumerate(t):
        m[i] = n // money
        n = n % money
        print(m, n)
    return m,n

#print(change(t, 41))
cash = input("請輸入零錢數")

while True:
    if(cash.isdigit()):
        cash = int(cash)
        break
    else:
        cash = input("請輸入零錢數")
change(t, cash)
print("===" * 10)

#動態規劃版
t = [25, 20, 5, 1]
def getMinCounts(k, values):
    memo = [-1] * (k + 1)
    memo[0] = 0 # 初始化狀態
    #print(memo)
    for item in range(1, k + 1):
       memo[item] = k + 1
    #print(memo)
    for item in range(1, k + 1):
        for coin in values:
            if (item - coin < 0):
                continue
            memo[item] = min(memo[item], memo[item - coin] + 1) # 作出決策
    #print(memo)
    return memo[k]

def getMinCountsDPSol():
    values = [25, 20, 5, 1] # 硬幣面值
    total = 61 # 總值

    # 求得最小的硬幣數量
    return getMinCounts(total, values) # 輸出答案

result = getMinCountsDPSol()
print("最少硬幣數：",result)
print("===" * 10)

#背包問題 貪婪法
number = 5
name = ['PS5', 'iPad pro 12', 'Macbook pro 15', 'HomePod', 'Mac mini']
weight = [5, 1, 4, 3, 2]
value = [17000, 35000, 60000, 9000, 20000]
count = 10

def greedy(n, w, v, c, m):
    initial = 0  #從一開始的重量
    total = 0    #總價值
    take = []    #拿走的商品
    while True:
        if(initial + w[v.index(max(v))] < c):  #如果可以拿走商品(<10)
            take.append(m[v.index(max(v))])        #拿走的商品名字
            initial += w[v.index(max(v))]       #拿走的總重量
            total += max(v)                     #總價值
            indexR = v.index(max(v))            #紀錄index
            v.pop(indexR)                       #拿走之後不可再拿,所以pop掉
            w.pop(indexR)
            m.pop(indexR)
            #print(v,w)
            #print(initial,total)
        else:
            break
    return (initial,total, take)
print(greedy(number, weight, value, count, name))
print("===" * 10)

#背包問題 動態規劃
# A Dynamic Programming based Python  
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can  
# be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
# Driver program to test above function 
val = [17000, 35000, 60000, 9000, 20000]
wt = [5, 1, 4, 3, 2] 
W = 10
n = len(val) 
print("最高價值：",knapSack(W, wt, val, n)) 
  
# This code is contributed by Bhavya Jain 










