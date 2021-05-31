# Uses python3
import sys

# def get_optimal_value(capacity, weights, values):
#     value = 0.
#     proportion = [float(v) / float(w) for v, w in zip(values, weights)]
#     for _ in range(len(weights) + 1):
#         if capacity == 0:
#             return value
#             break
#         max_weight = max(proportion)
#         index = proportion.index(max_weight)
#         proportion[index] = -1
#         add_capacity = min(capacity, weights[index])
#         value += add_capacity * max_weight
#         # weights[index] -= add_capacity
#         capacity -= add_capacity
#     return value

def get_optimal_value(capacity, weights, values):
    # write your code here
    max_capacity = 0
    value_per_weight = [[weight,(float(value)/float(weight), value)] for value, weight in zip(values, weights)]
    # value_per_weight = sorted(value_per_weight.items(), key=lambda x: (-x[1][0], x[0]))
    value_per_weight = sorted(value_per_weight, key=lambda x: (x[1][0]), reverse=True)
    for weight, (_, value) in value_per_weight:
        if weight <= capacity:
            # print(weight, value, capacity, max_capacity)
            max_capacity += value
            capacity -= weight
            # print(weight, value, capacity, max_capacity)
        else:
            max_capacity += capacity * (float(value)/float(weight))
            break
    return round(max_capacity, 4)
  
get_optimal_value(10, [1,2,1],[9,9,9])
# get_optimal_value(60, [5,10,15,22,25], [30,40,45,77,90])
# get_optimal_value(50, [20,50,30], [60,100,120])
# get_optimal_value(8,[3,2,2],[1.65,1,1])

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
