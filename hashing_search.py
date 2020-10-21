import random

INDEXBOX = 10
MAXNUM=7

def print_data(data, max_number):
    print('\t', end='')
    for i in range(max_number):
        print('[%2d]' %data[i], end='')
    print()

def create_table(num, index):
    tmp=num%INDEXBOX
    while True:
        if index[tmp]==-1:
            index[tmp]=num
            break
        else:
            tmp=(tmp+1)%INDEXBOX

def quadratic_table(num, index):
    time = 0
    tmp=num%INDEXBOX
    while True:
        time += 1
        if index[tmp]==-1:
            index[tmp]=num
            break
        else:
            tmp=num%INDEXBOX
            tmp=(tmp+(time*time))%INDEXBOX

def rehashing_table(num, index):
    tmp=num%INDEXBOX
    time = 0  # we suppose that our rahashing function is h1(x)=(x+2) mod b and so on
    while True:
        if index[tmp]==-1:
            index[tmp]=num
            break
        else:
            time += 1
            tmp=num%INDEXBOX
            tmp=(tmp+(time*2))%INDEXBOX

#Main

index=[None]*INDEXBOX
data=[None]*MAXNUM

print('原始陣列值')
for i in range(MAXNUM):
    data[i]=random.randint(1,20)
for i in range(INDEXBOX):
    index[i]=-1
print_data(data, MAXNUM)

print("線性雜湊表內容：")
for i in range(MAXNUM):
    create_table(data[i], index)
    print('  %2d =>' %data[i], end='')
    print_data(index, INDEXBOX)

print('完成現性雜湊表')
print_data(index, INDEXBOX)
print("\n\n")

index=[None]*INDEXBOX
data=[None]*MAXNUM

print('原始陣列值')
for i in range(MAXNUM):
    data[i]=random.randint(1,20)
for i in range(INDEXBOX):
    index[i]=-1
print_data(data, MAXNUM)

print("平方雜湊表內容：")
for i in range(MAXNUM):
    quadratic_table(data[i], index)
    print('  %2d =>' %data[i], end='')
    print_data(index, INDEXBOX)

print('完成平方雜湊表')
print_data(index, INDEXBOX)
print("\n\n")


index=[None]*INDEXBOX
data=[None]*MAXNUM

print('原始陣列值')
for i in range(MAXNUM):
    data[i]=random.randint(1,20)
for i in range(INDEXBOX):
    index[i]=-1
print_data(data, MAXNUM)

print("再雜湊表內容：")
for i in range(MAXNUM):
    rehashing_table(data[i], index)
    print('  %2d =>' %data[i], end='')
    print_data(index, INDEXBOX)

print('完成再雜湊表')
print_data(index, INDEXBOX)
print("\n\n")
