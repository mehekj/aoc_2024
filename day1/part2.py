def part2():
    with open("./input.txt", "r") as f:
        numbers = f.read().split()
    left = [int(i) for i in numbers[::2]]
    right = [int(i) for i in numbers[1::2]]

    right_occurrences = {}
    for num in right:
        if num not in right_occurrences:
            right_occurrences[num] = 0
        right_occurrences[num] += 1

    score = 0
    for num in left:
        if num not in right_occurrences:
            continue
        else:
            score += num * right_occurrences[num]

    print(score)


part2()
