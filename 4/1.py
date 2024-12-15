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

            # horizontal left to right 
            if j+3 < rowLength and lines[i][j] == 'X' and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
                result += 1

            # horizontal right to left
            if j-3 >= 0 and lines[i][j] == 'X' and lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
                result += 1

            # vertical top to bottom
            if i+3<lengthLines and lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
                result += 1

            # vertical bottom to top
            if i-3>=0 and lines[i][j] == 'X' and lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
                result += 1

            # diagonal top left to bottom right
            if i+3<lengthLines and j+3<rowLength and lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                result += 1
            
            # diagonal bottom right to top left
            if i-3>=0 and j-3>=0 and lines[i][j] == 'X' and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
                result += 1

            # diagonal top right to bottom left
            if i+3<lengthLines and j-3>=0 and lines[i][j] == 'X' and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
                result += 1

            # diagonal bottom left to top right
            if i-3>=0 and j+3<rowLength and lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
                result += 1

    return result


# read and test file input
if(False):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))