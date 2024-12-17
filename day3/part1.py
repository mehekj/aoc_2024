import re


def main():
    total = 0
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            for match in re.finditer(r"mul\(\d+,\d+\)", line):
                nums = re.findall(r"\d+", match.group(0))
                total += int(nums[0]) * int(nums[1])

    print(total)


main()
