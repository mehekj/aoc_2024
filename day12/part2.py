def valid(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def check_corner(grid, row, col, dir, char):
    up = None if not valid(
        grid, row + dir[0], col) else grid[row + dir[0]][col]
    left = None if not valid(
        grid, row, col + dir[1]) else grid[row][col + dir[1]]
    diagonal = None if not valid(
        grid, row + dir[0], col + dir[1]) else grid[row + dir[0]][col + dir[1]]

    # - -
    # - A
    if up is None and left is None:
        return True

    # - -
    # B A
    if up is None and left is not None and left != char:
        return True

    # - B
    # - A
    if up is not None and left is None and up != char:
        return True

    # * B
    # B A
    if up != char and left != char:
        return True

    # B A
    # A A
    if up == left and up == char and diagonal != char:
        return True

    return False


def calc_dims(grid, visited, row, col, dims):
    dims[0] += 1

    char = grid[row][col]
    visited[row][col] = 1

    dirs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    for dir in dirs:
        if check_corner(grid, row, col, dir, char):
            dims[1] += 1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in dirs:
        r = row + dir[0]
        c = col + dir[1]

        if valid(grid, r, c) and grid[r][c] == char and not visited[r][c]:
            calc_dims(grid, visited, r, c, dims)


def main():
    grid = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            grid.append(line.strip())

    visited = [[0] * len(grid[0]) for row in grid]
    dims = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not visited[row][col]:
                dims.append([0, 0])
                calc_dims(grid, visited, row, col, dims[-1])

    total = 0
    for dim in dims:
        total += dim[0] * dim[1]

    print(total)


main()
