text_sample = """3   4
4   3
2   5
1   3
3   9
3   3"""

def solve(input):
    result = 0
    lines: str = input.split("\n")

    leftMap={}
    rightMap={}
    lengthLines = len(lines)
    for i in range(lengthLines):
        values = lines[i].split()

        leftValue = int(values[0])
        leftMap[leftValue] = leftMap.get(leftValue, 0) + 1

        rightValue = int(values[1])
        rightMap[rightValue] = rightMap.get(rightValue, 0) + 1

    for i in range(lengthLines):
        min_left_key = min(leftMap.keys(), )
        min_right_key = min(rightMap.keys(), )

        result += min_left_key * rightMap.get(min_left_key, 0)

        if(leftMap[min_left_key] == 1): 
            leftMap.pop(min_left_key) 
        else:
            leftMap[min_left_key] -= 1

    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))