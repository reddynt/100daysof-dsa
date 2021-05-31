# Uses python3
import sys
from collections import namedtuple
from functools import reduce

Segment = namedtuple('Segment', 'start end')

def intersection(x, y):
    x_range = range(x[0], x[-1]+1)
    y_range = range(y[0], y[-1]+1)
    common_points = []
    if y_range[0] in x_range:
        common_points_start = y[0]
        if x_range[-1] <= y_range[-1]:
            common_points_end = x_range[-1]
        else:
            common_points_end = y_range[-1]
        common_points = [common_points_start, common_points_end]
    else:
        common_points = []
    if common_points:
        common_points = sorted(list(common_points))
        return [common_points[0], common_points[-1]]
    else:
        points.append(x)
        return y


def optimal_points(segments):
    global points
    points = []
    # write your code here
    segments = [[x, y] for x,y in segments]
    segments = sorted(segments, key=lambda x: (x[0], x[1]))
    reduce_value = reduce(lambda x, y: intersection(x, y), segments)
    points.append(reduce_value[-1])
    print(len(points))
    for point in points:
        if isinstance(point, list):
            print(point[-1], end=' ')
        else:
            print(point, end=' ')
    print('\n')


# optimal_points([[1,3],[2,5],[3,6]])
# optimal_points([[4,7],[1,3],[2,5],[5,6]])
# optimal_points(input)
# input = [[41, 42], [52, 52], [63, 63], [80, 82], [78, 79], [35, 35], [22, 23], [31, 32], [44, 45], [81, 82], [36, 38], [10, 12], [1, 1], [23, 23], [32, 33], [87, 88], [55, 56], [69, 71], [89, 91], [93, 93], [38, 40], [33, 34], [14, 16], [57, 59], [70, 72], [36, 36], [29, 29], [73, 74], [66, 68], [36, 38], [1, 3], [49, 50], [68, 70], [26, 28], [30, 30], [1, 2], [64, 65], [57, 58], [58, 58], [51, 53], [41, 41], [17, 18], [45, 46], [4, 4], [0, 1], [65, 67], [92, 93], [84, 85], [75, 77], [
#     39, 41], [15, 15], [29, 31], [83, 84], [12, 14], [91, 93], [83, 84], [81, 81], [3, 4], [66, 67], [8, 8], [17, 19], [86, 87], [44, 44], [34, 34], [74, 74], [94, 95], [79, 81], [29, 29], [60, 61], [58, 59], [62, 62], [54, 56], [58, 58], [79, 79], [89, 91], [40, 42], [2, 4], [12, 14], [5, 5], [28, 28], [35, 36], [7, 8], [82, 84], [49, 51], [2, 4], [57, 59], [25, 27], [52, 53], [48, 49], [9, 9], [10, 10], [78, 78], [26, 26], [83, 84], [22, 24], [86, 87], [52, 54], [49, 51], [63, 64], [54, 54]]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
