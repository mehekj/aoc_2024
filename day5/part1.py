def get_inputs():
    rules = []
    updates = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            if line.strip() == "":
                continue
            elif "|" in line:
                nums = line.split("|")
                rules.append((int(nums[0]), int(nums[1])))
            else:
                updates.append([int(i) for i in line.strip().split(",")])

    return rules, updates


def valid(update, before):
    for i in range(len(update) - 1):
        for after in update[i + 1:]:
            if update[i] in before and after in before[update[i]]:
                return False

    return True


def main():
    rules, updates = get_inputs()
    total = 0
    before = {}
    for rule in rules:
        if rule[1] not in before:
            before[rule[1]] = []
        before[rule[1]].append(rule[0])

    for update in updates:
        if valid(update, before):
            total += update[len(update) // 2]

    print(total)


main()
