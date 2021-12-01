
counter = 0

with open("input1.txt") as filestream:
    fileLines = filestream.readlines()
    
    comparator = int(fileLines[0].rstrip("\n"))
    for index in range(1, len(fileLines)):
        comparee = int(fileLines[index])
        if(comparee > comparator):
            counter += 1
        comparator = int(fileLines[index])

print(counter)