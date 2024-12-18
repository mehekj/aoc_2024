def get_input():
    robots = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            textparts = line.strip().split()
            p = textparts[0][textparts[0].find("=") + 1:].split(",")
            v = textparts[1][textparts[1].find("=") + 1:].split(",")

            robots.append([int(p[0]), int(p[1]), int(v[0]), int(v[1])])

    return robots


def move_robot(robot, w, h):
    newx = (robot[0] + robot[2]) % w
    newy = (robot[1] + robot[3]) % h
    robot[0] = newx
    robot[1] = newy


def main():
    w = 101
    h = 103

    robots = get_input()

    for i in range(100):
        for robot in robots:
            move_robot(robot, w, h)

    # 2 1
    # 3 4
    q1, q2, q3, q4 = 0, 0, 0, 0
    midx = w // 2
    midy = h // 2
    for robot in robots:
        if robot[0] == midx or robot[1] == midy:
            continue
        elif robot[1] < midy:
            if robot[0] > midx:
                q1 += 1
            elif robot[0] < midx:
                q2 += 1
        elif robot[1] > midy:
            if robot[0] < midx:
                q3 += 1
            elif robot[0] > midx:
                q4 += 1

    print(q1 * q2 * q3 * q4)


main()
