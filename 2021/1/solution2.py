
counter = 0

with open("input1.txt") as filestream:
    fileLines = filestream.readlines()
    
    comparator = int(fileLines[0].rstrip("\n")) + int(fileLines[1].rstrip("\n")) + int(fileLines[2].rstrip("\n"))
    for index in range(1, len(fileLines) - 2):
        comparee = int(fileLines[index]) + int(fileLines[index + 1]) + int(fileLines[index + 2])
        if(comparee > comparator):
            counter += 1
        comparator = comparee

print(counter)