def valid(row, col, w, h):
    return row >= 0 and row < h and col >= 0 and col < w


def main():
    antennas = {}
    antinodes = []
    with open("./input.txt", "r") as f:
        for row, line in enumerate(f.readlines()):
            antinodes.append([])
            for col, char in enumerate(line.strip()):
                antinodes[row].append(0)
                if char != '.':
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((row, col))

    h = len(antinodes)
    w = len(antinodes[0])
    for char, positions in antennas.items():
        for i, pos1 in enumerate(positions):
            for _, pos2 in enumerate(positions[i + 1:]):
                node1 = (2 * pos2[0] - pos1[0], 2 * pos2[1] - pos1[1])
                if valid(node1[0], node1[1], w, h):
                    antinodes[node1[0]][node1[1]] = 1

                node2 = (2 * pos1[0] - pos2[0], 2 * pos1[1] - pos2[1])
                if valid(node2[0], node2[1], w, h):
                    antinodes[node2[0]][node2[1]] = 1

    print(sum([sum(row) for row in antinodes]))


main()
