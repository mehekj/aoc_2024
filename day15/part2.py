def get_input():
    grid = []
    moves = ""
    pos = (-1, -1)

    with open("./input.txt", "r") as f:
        for row, line in enumerate(f.readlines()):
            if len(line.strip()) == 0:
                continue
            elif line[0] == '#':
                grid.append([])
                for col, char in enumerate(line.strip()):
                    if char == '@':
                        pos = (row, col * 2)
                        grid[row].append('@')
                        grid[row].append('.')
                    elif char == 'O':
                        grid[row].append('[')
                        grid[row].append(']')
                    else:
                        grid[row].append(char)
                        grid[row].append(char)
            else:
                moves += line.strip()

    return grid, moves, pos


def can_move_box(grid, left, right, dir):
    newleft = (left[0] + dir[0], left[1] + dir[1])
    newright = (right[0] + dir[0], right[1] + dir[1])
    leftchar = grid[newleft[0]][newleft[1]]
    rightchar = grid[newright[0]][newright[1]]

    if leftchar == '#' or rightchar == '#':
        return False
    elif leftchar == '.' and rightchar == '.':
        return True
    else:
        movable = True
        if leftchar == '[' and rightchar == ']':
            movable &= can_move_box(grid, newleft, newright, dir)
        if leftchar == ']':
            movable &= can_move_box(
                grid, (newleft[0], newleft[1] - 1), newleft, dir)
        if rightchar == '[':
            movable &= can_move_box(
                grid, newright, (newright[0], newright[1] + 1), dir)

        return movable


def move_box(grid, left, right, dir):
    newleft = (left[0] + dir[0], left[1] + dir[1])
    newright = (right[0] + dir[0], right[1] + dir[1])
    leftchar = grid[newleft[0]][newleft[1]]
    rightchar = grid[newright[0]][newright[1]]

    if dir == (0, -1):
        if leftchar == '#':
            return False
        elif leftchar == '.':
            grid[newleft[0]][newleft[1]] = '['
            grid[newright[0]][newright[1]] = ']'
            grid[right[0]][right[1]] = '.'
            return True
        elif leftchar == ']':
            if move_box(grid, (newleft[0], newleft[1] - 1), newleft, dir):
                grid[newleft[0]][newleft[1]] = '['
                grid[newright[0]][newright[1]] = ']'
                grid[right[0]][right[1]] = '.'
                return True

    elif dir == (0, 1):
        if rightchar == '#':
            return False
        elif rightchar == '.':
            grid[newleft[0]][newleft[1]] = '['
            grid[newright[0]][newright[1]] = ']'
            grid[left[0]][left[1]] = '.'
            return True
        elif rightchar == '[':
            if move_box(grid, newright, (newright[0], newright[1] + 1), dir):
                grid[newleft[0]][newleft[1]] = '['
                grid[newright[0]][newright[1]] = ']'
                grid[left[0]][left[1]] = '.'
                return True

    elif dir[1] == 0:
        if leftchar == '#' or rightchar == '#':
            return False
        elif leftchar == '.' and rightchar == '.':
            grid[newleft[0]][newleft[1]] = '['
            grid[newright[0]][newright[1]] = ']'
            grid[left[0]][left[1]] = '.'
            grid[right[0]][right[1]] = '.'
            return True
        else:
            movable = True
            if leftchar == '[' and rightchar == ']':
                movable &= can_move_box(grid, newleft, newright, dir)
            if leftchar == ']':
                movable &= can_move_box(
                    grid, (newleft[0], newleft[1] - 1), newleft, dir)
            if rightchar == '[':
                movable &= can_move_box(
                    grid, newright, (newright[0], newright[1] + 1), dir)

            if movable:
                if leftchar == '[' and rightchar == ']':
                    move_box(grid, newleft, newright, dir)
                if leftchar == ']':
                    move_box(grid, (newleft[0], newleft[1] - 1), newleft, dir)
                if rightchar == '[':
                    move_box(grid, newright,
                             (newright[0], newright[1] + 1), dir)

                grid[newleft[0]][newleft[1]] = '['
                grid[newright[0]][newright[1]] = ']'
                grid[left[0]][left[1]] = '.'
                grid[right[0]][right[1]] = '.'

                return True

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

    if newchar == '[':
        if move_box(grid, newpos, (newpos[0], newpos[1] + 1), dir):
            grid[newpos[0]][newpos[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            return newpos

    if newchar == ']':
        if move_box(grid, (newpos[0], newpos[1] - 1), newpos, dir):
            grid[newpos[0]][newpos[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            return newpos

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
            if char == '[':
                total += 100 * row + col

    print(total)


main()
