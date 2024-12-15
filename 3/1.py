import re
text_sample = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

def solve(input):
    result = 0

    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input)

    for match in matches:
        result += int(match[0]) * int(match[1])
        # print(match) 
    
    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))