from collections import Counter
import heapq
import os


def part_one():
    left = []
    right = []
    with open(os.path.join("inputs", "1.txt")) as f:
        for line in f:
            first, second = line.split()
            heapq.heappush(left, int(first))
            heapq.heappush(right, int(second))

    sum_of_distance_between_smallest = 0
    while left and right:
        sum_of_distance_between_smallest += abs(
            heapq.heappop(right) - heapq.heappop(left)
        )
    print(sum_of_distance_between_smallest)


part_one()


def part_two():
    left = []
    right = Counter()
    with open(os.path.join("inputs", "1.txt")) as f:
        for line in f:
            first, second = line.split()
            left.append(int(first))
            right[int(second)] += 1

    similarity_score = 0
    for num in left:
        similarity_score += num * right[num]
    print(similarity_score)


part_two()
