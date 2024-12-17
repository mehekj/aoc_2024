def main():
    with open("./input.txt", "r") as f:
        numbers = f.read().split()
    left = sorted([int(i) for i in numbers[::2]])
    right = sorted([int(i) for i in numbers[1::2]])

    distance = sum([abs(x - y) for x, y, in zip(left, right)])
    print(distance)


main()
