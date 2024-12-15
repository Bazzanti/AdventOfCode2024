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
        
    # print(leftMap)
    # print(rightMap)

    for i in range(lengthLines):
        min_left_key = min(leftMap.keys(), )
        min_right_key = min(rightMap.keys(), )

        result += abs(min_left_key - min_right_key)

        if(leftMap[min_left_key] == 1): 
            leftMap.pop(min_left_key) 
        else:
            leftMap[min_left_key] -= 1

        if(rightMap[min_right_key] == 1):
            rightMap.pop(min_right_key)
        else:
            rightMap[min_right_key] -= 1

    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))