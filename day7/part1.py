def solve(terms, acc, target):
    if len(terms) == 0:
        return acc == target

    next = terms[0]
    return solve(terms[1:], acc + next, target) \
        or solve(terms[1:], acc * next, target)


def main():
    equations = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            nums = line.split(":")
            answer = int(nums[0])
            terms = [int(i) for i in nums[1].split()]
            equations.append((answer, terms))

    total = 0
    for equation in equations:
        if solve(equation[1][1:], equation[1][0], equation[0]):
            total += equation[0]

    print(total)


main()
