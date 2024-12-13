import collections
from collections import Counter

def day1():
    f = open("input.txt", "r")

    left = []
    right = []
    for line in f:
        line = line.split()
        left.append(line[0])
        right.append(line[1])

    left.sort()
    right.sort()

    right_count = Counter(right)
    print(right_count)
    total = 0
    for e in left:
        total += int(e) * int(right_count[e])

    print(total)




    

day1()
