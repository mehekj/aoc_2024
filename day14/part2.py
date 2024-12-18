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


# i did look up a hint for this one i was lazy lol
def check_tree(robots, w, h):
    grid = [[0 for i in range(w)] for j in range(h)]
    for robot in robots:
        grid[robot[1]][robot[0]] += 1

    for r in range(1, h - 1):
        for c in range(1, w - 1):
            block = True
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if grid[r + dy][c + dx] == 0:
                        block = False
            if block:
                return True, grid

    return False, grid


def main():
    w = 101
    h = 103

    robots = get_input()

    i = 0
    success, grid = check_tree(robots, w, h)
    while not success and i < 100000:
        i += 1
        for robot in robots:
            move_robot(robot, w, h)
        success, grid = check_tree(robots, w, h)

    for row in grid:
        r = ""
        for col in row:
            r += str(col) if col > 0 else '.'
        print(r)
    print()

    print(i)


main()
