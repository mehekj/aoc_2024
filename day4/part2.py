def valid(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def has_mas(grid, row, col, dir):
    prev_x = row - dir[0]
    prev_y = col - dir[1]
    next_x = row + dir[0]
    next_y = col + dir[1]

    if not valid(grid, prev_x, prev_y) or not valid(grid, next_x, next_y):
        return False

    if grid[prev_x][prev_y] == "M" and grid[next_x][next_y] == "S":
        return True

    return False


def xmas_search(grid):
    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "A":
                if (has_mas(grid, row, col, (1, 1)) or has_mas(grid, row, col, (-1, -1))) \
                        and (has_mas(grid, row, col, (-1, 1)) or has_mas(grid, row, col, (1, -1))):
                    total += 1

    return total


def main():
    grid = []
    f = open("./input.txt", "r")
    for line in f.readlines():
        grid.append(line.strip())

    print(xmas_search(grid))


main()
