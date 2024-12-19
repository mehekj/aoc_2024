def get_input():
    grid = []
    moves = ""
    pos = (-1, -1)

    with open("./input.txt", "r") as f:
        for row, line in enumerate(f.readlines()):
            if len(line.strip()) == 0:
                continue
            elif line[0] == '#':
                grid.append(list(line.strip()))
                for col, char in enumerate(line.strip()):
                    if char == '@':
                        pos = (row, col)
            else:
                moves += line.strip()

    return grid, moves, pos


def move_box(grid, pos, dir):
    newpos = (pos[0] + dir[0], pos[1] + dir[1])
    newchar = grid[newpos[0]][newpos[1]]

    if newchar == '#':
        return False

    if newchar == '.':
        grid[newpos[0]][newpos[1]] = 'O'
        grid[pos[0]][pos[1]] = '.'
        return True

    if newchar == 'O':
        if move_box(grid, newpos, dir):
            grid[newpos[0]][newpos[1]] = 'O'
            grid[pos[0]][pos[1]] = '.'
            return True
        else:
            return False

    # shouldn't reach here
    return False


def move_robot(grid, pos, move):
    dir = (0, 0)
    if move == '<':
        dir = (0, -1)
    elif move == '^':
        dir = (-1, 0)
    elif move == '>':
        dir = (0, 1)
    elif move == 'v':
        dir = (1, 0)

    newpos = (pos[0] + dir[0], pos[1] + dir[1])
    newchar = grid[newpos[0]][newpos[1]]

    if newchar == '#':
        return pos

    if newchar == '.':
        grid[newpos[0]][newpos[1]] = '@'
        grid[pos[0]][pos[1]] = '.'
        return newpos

    if newchar == 'O':
        if move_box(grid, newpos, dir):
            grid[newpos[0]][newpos[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            return newpos
        else:
            return pos

    # shouldn't reach here
    return pos


def print_grid(grid):
    for row in grid:
        line = ""
        for char in row:
            line += char
        print(line)
    print()


def main():
    grid, moves, pos = get_input()

    for move in moves:
        pos = move_robot(grid, pos, move)

    total = 0
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == 'O':
                total += 100 * row + col

    print(total)


main()
