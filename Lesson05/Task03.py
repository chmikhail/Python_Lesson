from collections import defaultdict

data = defaultdict(int)

with open('Task03.ini') as fin:
    for line in fin:
        k, v = line.strip().split()
        data[k] = v
for value in data.values():
    value=int(value)
    if value >= 20000:
        print(value)
