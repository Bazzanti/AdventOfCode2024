from typing import List,Dict

text_sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def solve(input: str) -> int:
    result = 0

    parts = input.split("\n\n")
    sortings: List[str] = parts[0].split("\n")
    updates: List[str] = parts[1].split("\n")

    mapSortings: Dict[int, List[int]] = {}
    for i in range(len(sortings)):
        # print(sortings[i])

        left, right = map(int, sortings[i].split("|"))
        if left not in mapSortings:
            mapSortings[left] = []
        mapSortings[left].append(right)

    for j in range(len(updates)):
        updateRow = [int(s) for s in updates[j].split(",")]
        # print(updateRow)

        isok = True
        for k in range(len(updateRow)-1):
            # print(updateRow[k])
            if(updateRow[k] not in mapSortings or updateRow[k+1] not in mapSortings[updateRow[k]]):
                isok = False
                break


        if isok:
            middleOfList = updateRow[int((len(updateRow) - 1)/2)]
            print(middleOfList)
            result += middleOfList

    # print(mapSortings)

    return result


# read and test file input
if(True):
    file = open("input.txt", "r")
    input = file.read()
    print(solve(input)) # 
else:
    print(solve(text_sample))