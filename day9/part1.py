def construct_disk():
    with open("./input.txt", "r") as f:
        diskmap = f.read().strip()

    blocks = []
    file = True
    idx = 0
    for digit in diskmap:
        if file:
            blocks += [idx] * range(int(digit))
            idx += 1
        else:
            blocks += [-1] * range(int(digit))
        file = not file

    return blocks


def main():
    blocks = construct_disk()

    left = 0
    right = len(blocks) - 1
    while left < right:
        if blocks[left] < 0:
            blocks[left] = blocks[right]
            blocks[right] = -1
            while blocks[right] < 0:
                right -= 1
        left += 1

    total = 0
    for pos, id in enumerate(blocks):
        if id >= 0:
            total += pos * id

    print(total)


main()
