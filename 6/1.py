from typing import List,Dict

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

def solve(input: str) -> int:
    result = 0

    lines = [list(line) for line in input.split("\n")]

    # find ˆ
    xindex = -1
    yindex = -1
    for i in range(len(lines)):
        # print(lines[i])

        if "^" in lines[i]:
            xindex = lines[i].index("^")
            yindex = i
            break

    print(xindex, yindex)
    # loop and color
    direction = 0
    lines[yindex][xindex] = "X"

        #while yindex < len(lines) and xindex < len(lines[0]) :
    try:    #lazy
        while True:
            if direction == 0:
                if lines[yindex-1][xindex] == "#":
                    direction = 1
                else:
                    yindex -= 1
                    lines[yindex][xindex] = "X"
            elif direction == 1:
                if lines[yindex][xindex+1] == "#":
                    direction = 2
                else:
                    xindex += 1
                    lines[yindex][xindex] = "X"
            elif direction == 2:
                if lines[yindex+1][xindex] == "#":
                    direction = 3
                else:
                    yindex += 1
                    lines[yindex][xindex] = "X"
            elif direction == 3:
                if lines[yindex][xindex-1] == "#":
                    direction = 0
                else:
                    xindex -= 1
                    lines[yindex][xindex] = "X"
    except Exception as e:
        print(e)
        pass

    # print(lines)

    # count X
    for z in range(len(lines)):
        for w in range(len(lines[z])):
            if lines[z][w] == "X":
                result += 1

    return result

# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))