import csv
"""
1.import queue class since I'll use a priority queue to implement A* search
"""
import queue
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'

def astar(start, end):
    # Begin your code (Part 4)
    """
    2.declare a dictionary graph as a representation of the map
    3.declare a dictionary prenode to record the tuples (previous node, path cost + goal proximity) 
    4.read the data from edges.csv, note that the first line should be skipped, which is the header
    5.arrange some space in graph[] and prenode[] for the nodes being read 
    6.in graph[node1][node2], store the distance between them, note that the distance should in float type
    """
    graph = dict()
    prenode = dict()
    
    with open(edgeFile) as source1:
      reader = csv.reader(source1, delimiter=',', quotechar='"')
      for line in reader:
        data = line
        if data[0] == 'start':
          continue

        if data[0] not in graph:
          graph[data[0]] = dict()  
        if data[1] not in graph:
          graph[data[1]] = dict()
        prenode[data[0]] = (0,0.0)
        prenode[data[1]] = (0,0.0)
        
        graph[data[0]][data[1]] = float(data[2])
    """
    7.declare a dictionary h to store the heuristic function(straight-line distance)
    8.read the data from heuristic.csv, and get the ID of three end nodes from the header
    9.arrange some space in h[] for the nodes being read 
    10.in h[current node][end node], store the goal proximity, note that the distance should in float type
    """
    
    h = dict()
    case = 0

    with open(heuristicFile) as source2:
      reader = csv.reader(source2, delimiter=',', quotechar='"')
      for line in reader:
        data = line
        if data[0] == 'node':
          for i in range(1, 4):
            if data[i] == str(end):
              case = i
              break
          continue 
        h[data[0]] = float(data[case])
    
    """
    11.initiate path, num_visited
    12.initiate frontier, which is a prioity queue,
     with tuple (key,element) = (path cost + goal proximity, current node)
    13.push the start node(path cost = 0) in frontier
    14.begin to implement A*: first pop a tuple from the frontier and increment num_visited by one
    15.if it is the end node, get the final dist and finish the search
      (,since now the goal proximity = 0, we can get dist directly from the cost) 
    16.otherwise, for every adjancent nodes, calculate the total distance plus goal proximity
    17.if the adjancent node hasn't been visited or the total cost is lower than the former record,
      rewrite its prenode as (current node, new cost), and push it in the queue
    """ 
    path = list()
    num_visited = 0

    frontier = queue.PriorityQueue()
    frontier.put( (0.0+h[str(start)],str(start)) )

    while frontier.empty() == 0:
      current = frontier.get()
      num_visited = num_visited + 1
      if current[1] == str(end):
        dist = current[0]
        break
      for neighbor in graph[current[1]]:
        cost = current[0] + graph[current[1]][neighbor] - h[current[1]] + h[neighbor]
        if prenode[neighbor][0] == 0:
          prenode[neighbor] = (current[1], cost)
          frontier.put( (cost, neighbor) )
        elif cost < prenode[neighbor][1]:
          prenode[neighbor] = (current[1], cost)
          frontier.put( (cost, neighbor) )
    """
    18.reconstruct the path from the end node
    19.append the visited nodes to path according to the sequence record in prenode[][0]
    20.don't forget to append the start node before finish
    21.reverse path, then return all the required data
    """
    current = str(end) 
    while current != str(start):
      path.append(int(current))
      current = prenode[current][0]
    path.append(start)

    path.reverse()
    return path, format(dist,'.3f'), num_visited
    # End your code (Part 4)

if __name__ == '__main__':
    path, dist, num_visited = astar(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
