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


def sort_update(update, rules):
    nodes = {}
    for num in update:
        nodes[num] = []

    for rule in rules:
        if rule[0] in nodes and rule[1] in nodes:
            nodes[rule[1]].append(rule[0])

    nodes = sorted(nodes.items(), key=lambda item: len(item[1]))

    return [pair[0] for pair in nodes]


def main():
    rules, updates = get_inputs()
    total = 0
    before = {}
    for rule in rules:
        if rule[1] not in before:
            before[rule[1]] = []
        before[rule[1]].append(rule[0])

    for update in updates:
        sorted_update = sort_update(update, rules)
        if sorted_update != update:
            total += sorted_update[len(sorted_update) // 2]

    print(total)


main()
