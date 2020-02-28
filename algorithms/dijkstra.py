import copy


def dijkstra_alg(graph, start, end):
    infinity = float("inf")
    shortest_distance = {}
    predecessor = {}
    visiting_nodes = copy.copy(graph)
    path = []

    for node in visiting_nodes:
        shortest_distance[node] = infinity
    shortest_distance[str(start)] = 0

    steps = 0
    while visiting_nodes:
        # select the current node with tem min path
        # for the first iteration of the while loop, the minNode is start node
        # after first iteration, minNode is the node with minimum relaxed weight value
        minNode = None
        for node in visiting_nodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        # relax all the nodes that are connected to minNode
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        visiting_nodes.pop(minNode)
        steps += 1

    # get the path from start - end
    currentNode = str(end)
    while currentNode != str(start):
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("end node %s is not reachable from start node %s" % (end, start))
            break
    path.insert(0, currentNode)
    if shortest_distance[str(end)] != infinity:
        return [shortest_distance[str(end)], path, steps]
    else:
        return False
