import datetime
import matplotlib.pyplot as plt
import os
import random
import numpy as np
from Graph import Graph

graphs_list = ["graph100_0.1", "graph100_0.2", "graph100_0.3", "graph100_0.4",
               "graph200_0.1", "graph200_0.2", "graph200_0.3", "graph200_0.4",
               "graph500_0.1", "graph500_0.2", "graph500_0.3", "graph500_0.4",
               "graph1000_0.1", "graph1000_0.2", "graph1000_0.3", "graph1000_0.4",
               "graph2000_0.1", "graph2000_0.2", "graph2000_0.3", "graph2000_0.4",
               ]


def start_testing(g):
    """
    generate 10 pairs of nodes;
    if not reachable, generate again until success
    :param g: Graph instance
    :return:
    """
    n = 0
    dijkstra_time = 0
    astar_time = 0
    while n < 10:
        random_points = random.sample(g.vertices, 2)
        start = random_points[0]
        end = random_points[1]
        dijkstra_result = g.dijkstra(start, end)
        astar_result = g.a_star(start, end)
        if dijkstra_result[0] and astar_result[0]:
            n += 1
            dijkstra_time += dijkstra_result[1]
            astar_time += astar_result[1]
        else:
            continue
    return dijkstra_time, astar_time


def test():
    """
    test 10 pairs of nodes for each graph;
    generate an excel file to store test results
    generate a plot for performance analysis
    :return: None
    """
    result_path = os.path.join(os.getcwd(), "results")
    graph_path = os.path.join(os.getcwd(), "graphs")
    dijkstra_time_list = []
    astar_time_list = []
    for graph_code in graphs_list:
        each_graph_dir = os.path.join(graph_path, graph_code)
        g = Graph()
        for _, _, files in os.walk(each_graph_dir):
            for file in files:
                data_path = os.path.join(each_graph_dir, file)
                if file == "e.txt":
                    g.read_e(data_path)
                if file == "v.txt":
                    g.read_v(data_path)
            dijkstra_time, astar_time = start_testing(g)
            dijkstra_time_list.append(dijkstra_time)
            astar_time_list.append(astar_time)

    size = len(graphs_list)
    x = np.arange(size)
    total_width = 0.7
    n = 2
    width = total_width/n
    x = x - (total_width-width)/2

    plt.bar(x, dijkstra_time_list, width=width, label="Dijkstra", color="red", tick_label=graphs_list)
    plt.bar(x+width, astar_time_list, width=width, label="A*", color="green", tick_label=graphs_list)
    plt.xlabel("Graph Code")
    plt.ylabel("Time / seconds")
    plt.legend(loc="upper left")
    plt.title("Time Comparison (10 search operations)")
    plt.xticks(rotation=90)
    plt.rcParams["figure.figsize"] = (30, 15)

    now = datetime.datetime.now()
    sticker = now.strftime("%Y%m%d-%H%M%S")
    plt.savefig(result_path+"/"+sticker+".png", bbox_inches="tight")
    plt.show()


if __name__ == '__main__':
    test()
