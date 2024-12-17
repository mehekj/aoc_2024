def main():
    stones = []
    with open("./input.txt", "r") as f:
        stones = [int(i) for i in f.read().strip().split()]

    for i in range(25):
        newstones = []
        for stone in stones:
            if stone == 0:
                newstones.append(1)
            elif len(str(stone)) % 2 == 0:
                stonestr = str(stone)
                stonelen = len(stonestr) // 2
                newstones.append(int(stonestr[:stonelen]))
                newstones.append(int(stonestr[stonelen:]))
            else:
                newstones.append(2024 * stone)

        stones = newstones

    print(len(stones))


main()
