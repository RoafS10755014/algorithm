#sequential search

data=[20, 31, 50, 17, 16, 36, 19, 8]

def sequential_search(data, key):
    for i in data:
        if i == key:
            print("founded!")
            break
        if data.index(i) == len(data)-1:
            print("not found...")

sequential_search(data, 17)
sequential_search(data, 15)
        
