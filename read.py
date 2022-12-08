with open('test.txt', 'r') as objFile:
    lines = []

    for line in objFile:
        lines.append(line.strip())



print(lines)