with open("input.txt") as file:
    data = file.read().split("\n")
    data = [int(d) for d in data]
    data.append(0)
    data = sorted(data)
    data.append(max(data)+3)


differences = {1: 0, 2: 0, 3: 0}


# Getting all the differences
for i in range(len(data)-1):
    diff = data[i+1]-data[i]
    differences[diff] +=1

print(f"The 1st and 3rd differences multiplied: {differences[1]*differences[3]}")

# Part Two

ways = {}


def way_calc(i):
    if i == len(data)-1:
        return 1
    if i in ways:
        return ways[i]
    counter = 0
    for j in range(i+1, len(data)):
        if data[j]-data[i]<=3:
            counter += way_calc(j)
    ways[i] = counter
    return counter


print(f"The answer for part two: {way_calc(0)}")