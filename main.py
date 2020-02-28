import os
import random
from Graph import Graph


def main(graph_code, start, end):
    """

    :param graph_code: the code of graph files, for instance 100_0.1
    :param start: source node id
    :param end: destination node id
    :return: None
    """
    total_nodes_num = int(graph_code.split("_")[0])
    if start and end:

        if int(start) > total_nodes_num-1 or int(end) > total_nodes_num-1:
            print("Input nodes exceed total number of nodes, please select another")
        else:
            graphs_path = os.getcwd() + "/" + "graphs"
            v_file = graphs_path + "graph100_0.1" + "v.txt"
            e_file = graphs_path + "graph100_0.1" + "e.txt"
            for root, dirs, files in os.walk(graphs_path):
                for graph_dir in dirs:
                    if graph_code in graph_dir:
                        v_file = "/".join([graphs_path, graph_dir, "v.txt"])
                        e_file = "/".join([graphs_path, graph_dir, "e.txt"])

            g = Graph()
            g.read_e(e_file)
            g.read_v(v_file)
            print("---------------------------------")
            print("[INFO] Running dijkstra algorithm")
            g.dijkstra(start, end)
            print("---------------------------------")
            print("[INFO] Running A* algorithm")
            g.a_star(start, end)
    else:
        result = None
        while not result:
            random_points = random.sample(range(total_nodes_num), 2)
            start = random_points[0]
            end = random_points[1]


if __name__ == '__main__':
    while True:
        print("---------------------Program Start------------------------")
        graph_code = input("Enter Graph Code (100_0.1, 2000_0.4, etc): ")
        start = input("Enter source point: ")
        end = input("Enter destination point: ")
        main(graph_code, start, end)
