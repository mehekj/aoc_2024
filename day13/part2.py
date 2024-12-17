def get_inputs():
    with open("./input.txt", "r") as f:
        entries = f.read().split("\n\n")

    claws = []
    for entry in entries:
        lines = entry.split('\n')
        a_text = lines[0][lines[0].find('X+') + 2:].split(', Y+')
        b_text = lines[1][lines[1].find('X+') + 2:].split(', Y+')
        prize_text = lines[2][lines[2].find('X=') + 2:].split(', Y=')

        claws.append((int(a_text[0]), int(a_text[1]), int(b_text[0]), int(
            b_text[1]), int(prize_text[0]) + 10000000000000, int(prize_text[1]) + 10000000000000))

    return claws


def is_int(val, eps):
    return abs(val - round(val)) < eps


def cost(claw):
    Btop = claw[5] - claw[1] * claw[4] / claw[0]
    Bbottom = claw[3] - claw[1] * claw[2] / claw[0]

    B = Btop / Bbottom

    A = (claw[4] - claw[2] * B) / claw[0]

    if not is_int(A, 0.001) or not is_int(B, 0.001):
        return 0

    return 3 * round(A) + round(B)


def main():
    claws = get_inputs()

    total = 0
    for claw in claws:
        total += cost(claw)

    print(total)


main()
