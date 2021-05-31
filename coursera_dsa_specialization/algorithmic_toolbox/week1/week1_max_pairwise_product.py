n = int(input())
a = [int(x) for x in input().split()]

max_elem1 = max(a)
max_elem2 = 0


if a.count(max_elem1) > 1:
    max_elem2 = max_elem1
else:
    for i in a:
        if i == max_elem1:
            continue
        max_elem2 = max(max_elem2, i)

print(max_elem1 * max_elem2)
