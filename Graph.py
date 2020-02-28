from random import sample
from algorithms.dijkstra import dijkstra_alg
from algorithms.astar import astar_alg
from datetime import datetime
import time


class Graph(object):

    def __init__(self):
        self.end = None
        self.start = None
        self.graph = {}
        self.graph_square = {}
        self.vertices = []
    """
    represent graph as a dictionary; represent vertices's location as a dcitionary
    key -> vertex id as int
    1. value of graph -> a dictionary with keys that are:
        other nodes's index as int that current node is connected to, and value is the weight of edge
    example of graph:
    {
        0: {
            1: 10,
            2: 20,
        },
        1: {
            0: 10,
            2: 5
        }
        2: {
            1: 5,
            0: 20,
        }
    }
    2. value of graph_square -> a dictionary with vertex id as key and square number as value, all int.
        graph_square can be None if running uninformed search.
    example of graph_square
    {
        1: 10,
        2: 55,
        3: 99
    }
    """
    def clear(self):
        self.graph = {}
        self.graph_square = {}
        self.vertices = []

    def read_e(self, e_file):
        """
        Read edge file (e.txt) into defined structure
        :param e_file: absolute path of e.txt
        :return: None
        """
        with open(e_file, "r") as fe:
            lines = fe.readlines()
            for line in lines:
                line = line.strip()
                if line[0] != "#":
                    line_info = line.split(",")
                    start_v = line_info[0]
                    end_v = line_info[1]
                    weight = int(line_info[2])
                    if start_v not in self.graph:
                        self.graph[start_v] = {}
                        self.graph[start_v][end_v] = weight
                    else:
                        if end_v not in self.graph[start_v]:
                            self.graph[start_v][end_v] = weight
                    if end_v not in self.graph:
                        self.graph[end_v] = {}

            self.vertices = list(self.graph.keys())

    def read_v(self, v_file):
        """
        Read square file into defined structure
        :param v_file: absolute path of v.txt
        :return: None
        """
        with open(v_file, "r") as fv:
            lines = fv.readlines()
            for line in lines:
                line = line.strip()
                if line[0] != "#":
                    line_info = line.split(",")
                    index = line_info[0]
                    square = line_info[1]
                    self.graph_square[index] = square

            self.vertices = list(self.graph.keys())

    def generate_random_points(self):
        random_points = sample(self.vertices, 2)
        self.start = random_points[0]
        self.end = random_points[1]

    def dijkstra(self, start, end):
        if (not start) and (not end):
            self.generate_random_points()
            start = self.start
            end = self.end
            print("start node(random): ", str(start))
            print("goal node(random): ", str(end))
        else:
            print("start node: ", start)
            print("goal node: ", end)

        time_stamp1 = time.time()
        search_result = dijkstra_alg(self.graph, start, end)

        time_stamp2 = time.time()

        total_time_stamp = time_stamp2 - time_stamp1
        self.print_search_result(search_result, total_time_stamp, "dijkstra")
        return [search_result, total_time_stamp]

    def a_star(self, start, end):
        if (not start) and (not end):
            start = self.start
            end = self.end
            print("start node(random): ", str(start))
            print("goal node(random): ", str(end))
        else:
            print("start node: ", start)
            print("goal node: ", end)
        time_stamp1 = time.time()
        search_result = astar_alg(self.graph, self.graph_square, start, end)

        time_stamp2 = time.time()

        total_time_stamp = time_stamp2 - time_stamp1
        self.print_search_result(search_result, total_time_stamp, "A*")
        return [search_result, total_time_stamp]

    @staticmethod
    def print_search_result(search_result, time_stamp, type):
        if search_result:
            shortest_distance = search_result[0]
            shortest_path = search_result[1]
            steps = search_result[2]
            print("----------Result for %s-----------" % type)
            print("-Total searching time is:", str(time_stamp), "s")
            print("-Shortest distance is ", shortest_distance)
            print("-The path from start to end is", shortest_path)
            print("-Total searching steps:", steps)

        else:
            print("Algorithm failed")


if __name__ == '__main__':
    g = Graph()
    g.read_e(r"D:\GWU\2020Spring\6511Artificial_Intelligence-AmrinderArora\Project_1\graphs\graph2000_0.1\e.txt")
    g.read_v(r"D:\GWU\2020Spring\6511Artificial_Intelligence-AmrinderArora\Project_1\graphs\graph2000_0.1\v.txt")
    g.dijkstra("0", "55")
    g.a_star("0", "55")
    pass
