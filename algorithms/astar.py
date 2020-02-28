from math import sqrt


def astar_alg(graph, graph_square, start, end):
    # firstly, we need to calculate the heuristic measurement
    # which is the estimate of distance from each node to the end node
    # I am using Euclidean distance. But, in order to optimize, some conner cases
    # If two nodes are in a same square, the distance is also 14.1421 by definition

    # 1. calculate the Heuristic distance from each node to end node(h)
    end_square = graph_square[end]
    if len(end_square) == 1:
        end_square = "0" + end_square
    end_x = int(end_square[0])
    end_y = int(end_square[1])

    # generate end node's neighbors
    end_neighbor = []
    for n in [-1, 0, 1]:
        for m in [-1, 0, 1]:
            end_neighbor.append("".join([str(end_x+n), str(end_y+m)]))

    heuristic_distance = {}
    for node in graph_square:
        node_square = graph_square[node]

        if len(node_square) == 1:
            node_square = "0" + str(node_square)

        if node == end:
            h = 0
        elif node_square in end_neighbor:
            h = 0

        else:
            node_x = int(node_square[0])
            node_y = int(node_square[1])
            x_dis = node_x - end_x
            y_dis = node_y - end_y
            if x_dis != 0:
                x_dis -= 1
            if y_dis != 0:
                y_dis -= 1

            x_dis_square = x_dis ** 2
            y_dis_square = y_dis ** 2
            h = sqrt(x_dis_square + y_dis_square)
        heuristic_distance[node] = h

    # 2. initialize data structures
    # nodes to be search, with it's g value and f value. For the first node, g=0 and f=h
    frontier = {start: heuristic_distance[start]}
    # g value dictionary (how long to travel to this node)
    g_dict = {start: 0}
    # searched nodes
    closed_nodes = {}
    # store the path information {childNode: parentNode}
    predecessor = {}
    path = []
    # 3. start iteration
    # Note that frontier is like the visiting node in dijkstra
    steps = 0
    while frontier:
        # find node in open list(frontier) with least f value to be the current Node
        currentNode = min(frontier, key=frontier.get)
        # remove currentNode from frontier
        del frontier[currentNode]
        parentNode = currentNode
        # main loop: add currentNode's adjacent nodes to frontier
        for successor, weight in graph[currentNode].items():
            # check if successor is already visited
            if successor not in closed_nodes:
                # calculate f = g + h for each node and add to frontier
                g_node = weight + g_dict[parentNode]
                h_node = heuristic_distance[successor]
                f_node = g_node + h_node
                # check if a successor has a better f value

                if successor not in frontier or f_node < frontier[successor]:
                    steps += 1
                    frontier[successor] = f_node
                    predecessor[successor] = parentNode
                    g_dict[successor] = g_node
        closed_nodes[currentNode] = currentNode

        if currentNode == end:
            # get the path and cost
            cost = g_dict[currentNode]
            visited_nodes = []
            while currentNode != start:
                try:
                    path.insert(0, currentNode)
                    currentNode = predecessor[currentNode]
                except KeyError:
                    print("end node %d is not reachable from start node %d" % (end, start))
                    break
            path.insert(0, currentNode)
            for node in closed_nodes:
                visited_nodes.append(node)
            return [cost, path, steps, visited_nodes]
