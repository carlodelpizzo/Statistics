data = [2, 18, 23, 41, 44, 46, 49, 61, 62, 74, 76, 79, 82, 89, 92, 95]
split = 1/5

if 1/split > len(data):
    split = 1/len(data)

k = int(1/split)
split_points = []
split_values = []
for i in range(1, k):
    split = (i/k)*(len(data) + 1)
    if split % 1 != 0:
        split_1 = int(split) + 1
        split = int(split)
        split_points.append((split, split_1))
        value = (data[split - 1] + data[split_1 - 1]) / 2
        if value % 1 == 0:
            value = int(value)
        split_values.append(value)
    else:
        split_points.append(int(split))
        split_values.append(data[int(split) - 1])


print('The split points are: {}'.format(split_points))
print('The split values are: {}'.format(split_values))
