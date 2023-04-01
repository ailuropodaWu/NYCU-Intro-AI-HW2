import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
    file = open(edgeFile, 'r')
    csvFile = csv.reader(file)
    data = []
    header = []
    header = next(csvFile)
    for row in csvFile:
        data.append(row)
    file.close()
    graph = dict()
    visited = dict()
    for i in range(len(data)):
        data[i][0], data[i][1], data[i][2], data[i][3] = int(data[i][0]), int(data[i][1]), float(data[i][2]), float(data[i][3])
        visited[data[i][0]] = -1
        visited[data[i][1]] = -1
        if data[i][0] not in graph:
            graph[data[i][0]] = dict()
        if data[i][1] not in graph:
            graph[data[i][1]] = dict()
        graph[data[i][0]][data[i][1]] = (data[i][2], data[i][3])
    visited[start] = 0
    
    queue = []
    queue.append(start)
    dist = 0
    num_visited = 1
    flag = True
    while (len(queue) > 0 and flag):
        current = queue.pop(0)
        for neighbor in graph[current]:
            if visited[neighbor] == -1: 
                visited[neighbor] = current
                if neighbor == end:
                    flag = False
                    break                      
                queue.append(neighbor)
                num_visited += 1
    
    path = []
    current = end
    if not flag:
        while visited[current] != 0:
            path.append(visited[current])
            dist += graph[visited[current]][current][0]
            current = visited[current]
    path.append(current)
    path.reverse()
    return path, dist, num_visited
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
