with open("input.txt") as file:
    data = file.read().split("\n")
    data = sorted(int(d) for d in data)


# 3 starts at one because built in adapter
differences = {1: 0, 2: 0, 3: 1}

# Adding difference between start and first adapter
differences[data[0]] += 1

# Getting all the differences
for i in range(len(data)-1):
    diff = data[i+1]-data[i]
    differences[diff] +=1

print(f"The 1st and 3rd differences multiplied: {differences[1]*differences[3]}")