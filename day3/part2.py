import re


def main():
    total = 0
    enabled = True
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            for match in re.finditer(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", line):
                word = match.group(0)
                if word == "do()":
                    enabled = True
                elif word == "don't()":
                    enabled = False
                elif enabled:
                    nums = re.findall(r"\d+", match.group(0))
                    total += int(nums[0]) * int(nums[1])

    print(total)


main()
