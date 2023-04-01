import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    file = open(edgeFile, 'r')
    csvFile = csv.reader(file)
    next(csvFile)
    data = []
    for row in csvFile:
        data.append(row)
    file.close()
    graph = dict()
    visited = dict()
    cost = dict()
    for i in range(len(data)):
        data[i][0], data[i][1], data[i][2], data[i][3] = int(data[i][0]), int(data[i][1]), float(data[i][2]), float(data[i][3])
        visited[data[i][0]] = -1
        visited[data[i][1]] = -1
        if data[i][0] not in graph:
            graph[data[i][0]] = dict()
            cost[data[i][0]] = 10 ** 8
        if data[i][1] not in graph:
            graph[data[i][1]] = dict()
            cost[data[i][1]] = 10 ** 8
        graph[data[i][0]][data[i][1]] = (data[i][2], data[i][3]) 
    visited[start] = 0
    cost[start] = 0

    file = open(heuristicFile, 'r')
    csvFile = csv.reader(file)
    next(csvFile)
    data = []
    for row in csvFile:
        data.append(row)
    file.close()
    endPoint = []
    for i in range(len(data)):
        data[i][0], data[i][1], data[i][2], data[i][3] = int(data[i][0]), float(data[i][1]), float(data[i][2]), float(data[i][3])
        if data[i][0] == end:
            endPoint = data[i][1:]
            break
    
    heuristicCost = dict()
    for i in range(len(data)):
        heuristicCost[int(data[i][0])] = 0
        for j in range(3):
            if endPoint[j] == 0.0:
                heuristicCost[int(data[i][0])] = float(data[i][j+1]) ** 2
                break
            else:
                heuristicCost[int(data[i][0])] += (float(data[i][j+1]) - endPoint[j]) ** 2
        heuristicCost[int(data[i][0])] = pow(heuristicCost[int(data[i][0])], 0.5)
    
    queue = []
    queue.append(start)
    dist = 0
    num_visited = 1
    while len(queue) > 0:
        queue = sorted(queue, key=lambda x: cost[x] + heuristicCost[x])
        current = queue.pop(0)
        num_visited += 1
        if current == end:
            break
        for neighbor in graph[current]:
            temp = cost[current] + graph[current][neighbor][0]
            if visited[neighbor] == -1:
                visited[neighbor] = current
                cost[neighbor] = temp
                queue.append(neighbor)
            elif temp < cost[neighbor]:
                visited[neighbor] = current
                cost[neighbor] = temp
                queue.append(neighbor)

    path = []
    current = end
    while visited[current] != 0:
        path.append(visited[current])
        dist += graph[visited[current]][current][0]
        current = visited[current]
    path.append(current)
    path.reverse()
    return path, dist, num_visited
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
