def calc_stone(stone, totals, n):
    if not n in totals:
        totals[n] = {}

    if n == 0:
        totals[n][stone] = 1

    if stone in totals[n]:
        return totals[n][stone]

    if stone == 0:
        totals[n][stone] = calc_stone(1, totals, n - 1)
    elif len(str(stone)) % 2 == 0:
        stonestr = str(stone)
        stonelen = len(stonestr) // 2
        totals[n][stone] = calc_stone(int(stonestr[:stonelen]), totals, n - 1) \
            + calc_stone(int(stonestr[stonelen:]), totals, n - 1)
    else:
        totals[n][stone] = calc_stone(2024 * stone, totals, n - 1)

    return totals[n][stone]


def main():
    stones = []
    with open("./input.txt", "r") as f:
        stones = [int(i) for i in f.read().strip().split()]

    ans = 0
    totals = {}
    for stone in stones:
        ans += calc_stone(stone, totals, 75)

    print(ans)


main()
