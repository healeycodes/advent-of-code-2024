import os
import re


def part_one():
    with open(os.path.join("inputs", "3.txt")) as f:
        program = f.read()

    print(sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", program)))


part_one()


def part_two():
    with open(os.path.join("inputs", "3.txt")) as f:
        program = f.read()

    mul_matches = re.finditer(r"mul\((\d+),(\d+)\)", program)
    do_matches = re.finditer(r"do\(\)", program)
    dont_matches = re.finditer(r"don't\(\)", program)

    total = 0
    enabled = True
    for match in sorted(
        list(mul_matches) + list(do_matches) + list(dont_matches),
        key=lambda x: x.start(),
    ):
        if "mul" in match.group():
            if enabled:
                total += int(match.group(1)) * int(match.group(2))
        elif "do()" in match.group():
            enabled = True
        elif "don't()" in match.group():
            enabled = False
    print(total)


part_two()
