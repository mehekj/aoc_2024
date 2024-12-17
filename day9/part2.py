def construct_disk():
    with open("./input.txt", "r") as f:
        diskmap = f.read()

    blocks = {}
    frees = []
    file = True
    idx = 0
    pos = 0
    for digit in diskmap:
        blocksize = int(digit)
        if file:
            blocks[idx] = (pos, pos + blocksize)
            idx += 1
        else:
            frees.append((pos, pos + blocksize))

        pos += blocksize
        file = not file

    return blocks, frees


def main():
    blocks, frees = construct_disk()

    n = list(blocks.keys())[-1]

    for idx in range(n, 0, -1):
        blocksize = blocks[idx][1] - blocks[idx][0]
        for i, free in enumerate(frees):
            if free[0] > blocks[idx][0]:
                continue
            freesize = free[1] - free[0]
            if freesize == blocksize:
                blocks[idx] = free
                frees.remove(free)
                break
            elif freesize > blocksize:
                blocks[idx] = (free[0], free[0] + blocksize)
                frees[i] = (free[0] + blocksize, free[1])
                break

    total = 0
    for idx, block in blocks.items():
        for pos in range(block[0], block[1]):
            total += idx * pos

    print(total)


main()
