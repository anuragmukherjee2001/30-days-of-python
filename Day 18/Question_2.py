points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']

point = []
for i in points:
    j = int(i)
    point.append(j)

point.sort()

distance = point[len(points) - 1] - point[0]

print(distance)    