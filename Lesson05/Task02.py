lines = 0
words = 0
for line in open('Task02.ini', 'r'):
    lines += 1
    words += len(line)

print(lines)
print(words)
