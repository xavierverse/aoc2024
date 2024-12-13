import re

with open("input.txt") as f:
    s = f.read().strip()

x = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", s)
# print(x.group(1), x.group(2))
print(x)

enabled = True
total = 0
for y in x:
    print(y)
    # s = line.split()
    if y[2]  == "" and enabled:
        total += int(y[0]) * int(y[1])
    else:
        if y[2] == "do()":
            enabled = True
        else:
            enabled = False

print(total)

