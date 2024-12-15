text_sample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def solve(input):
    result = 0
    lines: str = input.split("\n")

    lengthLines = len(lines)
    correct = True
    for i in range(lengthLines):
        fullValues = [int(x) for x in lines[i].split(" ")]
        for z in range(len(fullValues)):
            correct = True
            values = fullValues[:z] + fullValues[z+1:]
            # print(values)

            if values[0] < values[-1]:
                # growing
                for j in range(len(values)):
                    if j == 0: continue
                    if j > 0 and values[j] > values[j - 1] and values[j] <= values[j - 1] + 3:
                        continue

                    correct = False
                    break

            else :
                # decreasing
                for j in range(len(values)):
                    if j == 0: continue
                    if j > 0 and values[j] < values[j - 1] and values[j] >= values[j - 1] - 3:
                        continue

                    correct = False
                    break

            if correct == True:
                break



        if correct == True:
            result += 1
        
        correct = True
        # print(i, ": ", result)

    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))