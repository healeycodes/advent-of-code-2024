import os


def invalid_report(report):
    return (
        not all(report[i] < report[i + 1] for i in range(len(report) - 1))
        and not all(report[i] > report[i + 1] for i in range(len(report) - 1))
        or not all(
            abs(report[i] - report[i + 1]) in range(1, 4)
            for i in range(len(report) - 1)
        )
    )


def part_one():
    with open(os.path.join("inputs", "2.txt")) as f:
        reports = [list(map(int, line.split())) for line in f]

    print(sum(0 if invalid_report(report) else 1 for report in reports))


part_one()


def part_two():
    with open(os.path.join("inputs", "2.txt")) as f:
        reports = [list(map(int, line.split())) for line in f]

    report_count = 0
    for report in reports:
        # lazy: use a permutation of the report
        for i in range(len(report)):
            permutation = report[:i] + report[i + 1 :]

            if invalid_report(permutation):
                continue

            report_count += 1
            break

    print(report_count)


part_two()
