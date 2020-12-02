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
