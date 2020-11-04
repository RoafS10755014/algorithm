#hanoi tower

def hanoi(time, start, temp, end):
    if time == 1:
        print(start, "-->", end, end="")
        runTime()
        return
    hanoi(time - 1, start, end, temp)
    print(start, "-->", end, end="")
    runTime()
    hanoi(time - 1, temp, start, end)

def runTime():
    global times
    times += 1
    print("  rumtimes:", times)
    
times = 0


hanoi(5, "A", "B", "C")
