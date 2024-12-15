text_sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def solve(input):
    result = 0

    lines = input.split("\n")

    lengthLines = len(lines)
    for i in range(lengthLines):
        rowLength = len(lines[i])
        # print(lines[i])

        for j in range(rowLength):
            #print("row: ", i, " column: ", j)

            if (lines[i][j] == 'A' and j+1 < rowLength and j-1 >=0 and i+1 < lengthLines and i-1 >= 0) and \
            ((lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') or (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M')) and \
            ((lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S') or (lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M')):
                result += 1

    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))