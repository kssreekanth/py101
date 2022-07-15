def towerofhanoi(numerDisk, start, end, aux):
    if numerDisk == 1:
        print("Move disk", numerDisk, "from", start, "to end", end)
        return
    towerofhanoi(numerDisk - 1, start, aux, end)
    print("Move disk", numerDisk, " from", start, "to end", end)
    towerofhanoi(numerDisk - 1, aux, end, start)


towerofhanoi(4, "A", "B", "C")
