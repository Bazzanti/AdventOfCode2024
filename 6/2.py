from copy import copy, deepcopy

text_sample = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def walkPathOnce(lines, xindex, yindex):
    walkedCells = []
    direction = 0
    
    try:
        while True:
            if direction == 0:
                if lines[yindex-1][xindex] == "#":
                    direction = 1
                else:
                    yindex -= 1
                    walkedCells.append([xindex, yindex])
            elif direction == 1:
                if lines[yindex][xindex+1] == "#":
                    direction = 2
                else:
                    xindex += 1
                    walkedCells.append([xindex, yindex])
            elif direction == 2:
                if lines[yindex+1][xindex] == "#":
                    direction = 3
                else:
                    yindex += 1
                    walkedCells.append([xindex, yindex])
            elif direction == 3:
                if lines[yindex][xindex-1] == "#":
                    direction = 0
                else:
                    xindex -= 1
                    walkedCells.append([xindex, yindex])
    except Exception as e:
        print("walked")
        print(e)
        pass

    walkedCells = [list(x) for x in set(tuple(x) for x in walkedCells)]
    return walkedCells

def solve(input: str) -> int:
    result = 0

    lines = [list(line) for line in input.split("\n")]

    # find ˆ
    startingXIndex = -1
    startingYIndex = -1
    for i in range(len(lines)):
        # print(lines[i])

        if "^" in lines[i]:
            startingXIndex = lines[i].index("^")
            startingYIndex = i
            break

    walkedPath = walkPathOnce(lines, startingXIndex, startingYIndex)

    for i in range(len(walkedPath)):

        if walkedPath[i][1] == startingYIndex and walkedPath[i][0] == startingXIndex:
            continue

        xindex = startingXIndex
        yindex = startingYIndex

        direction = 0
        alreadyvisited = []
        linesWithExtra = deepcopy(lines)
        linesWithExtra[walkedPath[i][1]][walkedPath[i][0]] = "#"


        try:    #lazy
            while True:      
                
                if {"x": xindex, "y": yindex, "d": direction} in alreadyvisited:
                    print("already visited", walkedPath[i][1], walkedPath[i][0], direction)
                    result +=1
                    break

                if direction == 0:
                    if linesWithExtra[yindex-1][xindex] == "#":
                        direction = 1
                    else:
                        alreadyvisited.append({"x": xindex, "y": yindex, "d": direction})
                        yindex -= 1
                elif direction == 1:
                    if linesWithExtra[yindex][xindex+1] == "#":
                        direction = 2
                    else:
                        alreadyvisited.append({"x": xindex, "y": yindex, "d": direction})
                        xindex += 1
                elif direction == 2:
                    if linesWithExtra[yindex+1][xindex] == "#":
                        direction = 3
                    else:
                        alreadyvisited.append({"x": xindex, "y": yindex, "d": direction})
                        yindex += 1
                elif direction == 3:
                    if linesWithExtra[yindex][xindex-1] == "#":
                        direction = 0
                    else:
                        alreadyvisited.append({"x": xindex, "y": yindex, "d": direction})
                        xindex -= 1
        except Exception as e:
            print(e, xindex, yindex, direction)
            pass

    return result

# read and test file input
if(False):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))

