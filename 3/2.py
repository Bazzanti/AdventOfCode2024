import re
text_sample = """do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def solve(input):
    result = 0

    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    matches = re.findall(pattern, input)

    print(matches)
    multiplier = 1
    for match in matches:
        if "do()" in match:
            multiplier = 1
            continue
        elif "don't()" in match:
            multiplier = 0
            continue

        print(match) 
        num1 = int(match[4:match.index(",")])
        num2 = int(match[match.index(",")+1:-1])
        result += num1 * num2 * multiplier
    
    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))
