def valid(grid, pos):
    return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])


def move(grid, pos, dir, visited):
    visited[pos[0]][pos[1]] = 1
    next = (pos[0] + dir[0], pos[1] + dir[1])
    if valid(grid, next) and grid[next[0]][next[1]] == '#':
        if dir == (0, 1):
            dir = (1, 0)
        elif dir == (1, 0):
            dir = (0, -1)
        elif dir == (0, -1):
            dir = (-1, 0)
        else:
            dir = (0, 1)

        next = (pos[0] + dir[0], pos[1] + dir[1])

    return next, dir, visited


def main():
    grid = []
    visited = []
    start = (-1, -1)
    with open("./input.txt", "r") as f:
        for row, line in enumerate(f.readlines()):
            grid.append(line.strip())
            visited.append([])
            for col, char in enumerate(line):
                visited[row].append(0)
                if char == "^":
                    start = (row, col)

    loops = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) == start or grid[row][col] == '#':
                continue

            newgrid = grid[:][:]
            newrow = list(grid[row])
            newrow[col] = '#'
            newgrid[row] = ''.join(newrow)

            pos = (start[0], start[1])
            dir = (-1, 0)
            vis = visited[:][:]
            tries = 0
            while valid(newgrid, pos) and tries < 25000:
                pos, dir, vis = move(newgrid, pos, dir, vis)
                tries += 1

            if valid(newgrid, pos) and tries >= 25000:
                print(row, col)
                loops += 1

    print(loops)


main()
