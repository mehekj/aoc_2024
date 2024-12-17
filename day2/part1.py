def is_safe(report):
    prevdiff = 0
    for i in range(len(report) - 1):
        curr = report[i]
        next = report[i + 1]
        diff = next - curr
        if prevdiff * diff < 0:
            prevdiff = diff
            return False
        prevdiff = diff
        if diff == 0:
            return False
        if abs(diff) > 3:
            return False

    return True


def main():
    safe = 0
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            report = [int(i) for i in line.split()]
            if is_safe(report):
                safe += 1

    print(safe)


main()