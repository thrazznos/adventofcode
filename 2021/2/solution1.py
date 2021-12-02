with open("input1.txt") as filestream:
    fileLines = filestream.readlines()

depth = 0
distance = 0

for line in fileLines:
    commands = line.split(' ')
    if(commands[0] == "forward"):
        distance += int(commands[1])
    if(commands[0] == "down"):
        depth += int(commands[1])
    if(commands[0] == "up"):
        depth -= int(commands[1])

print(depth * distance)