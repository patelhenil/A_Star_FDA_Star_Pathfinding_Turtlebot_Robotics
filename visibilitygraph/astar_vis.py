from graph import Point, Edge, Polygon, generate_visible_edges
from visline import intersection
from collections import defaultdict
import sys


class minHeap:

    def __init__(self):
        self.nodes = []
        self.size = 0
        self.p = []

    def Node(self, point, weight):
        node = [point, weight]
        return node

    def switch(self, node1, node2):
        n = self.nodes[node1]
        self.nodes[node1] = self.nodes[node2]
        self.nodes[node2] = n

    def heapify(self, index):
        min = index
        x = self.nodes[min][0]
        y = self.nodes[index][0]
        left = (2 * index) + 1
        right = (2 * index) + 1

        if left < self.size or right < self.size:
            if self.nodes[left][1] < self.nodes[min][1]:
                min = left
            if self.nodes[right][1] < self.nodes[min][1]:
                min = right

        if min != index:
            self.p[x] = index
            self.p[y] = min
            self.switch(min, index)
            self.heapify(min)

    def heapPop(self):
        if self.isEmpty():
            return None

        root = self.nodes[0]
        n = self.nodes[self.size - 1]
        self.nodes[0] = n
        self.p[n[0]] = 0
        self.p[root[0]] = self.size - 1
        self.size -= 1
        self.heapify(0)

        return root

    def isEmpty(self):
        return self.size <= 0

    def decreaseKey(self, v, weight):
        i = self.p[v]
        self.nodes[i][1] = weight
        x = int((i - 1) / 2)
        while i > 0 and self.nodes[i][1] < self.nodes[x][1]:
            self.p[self.nodes[i][0]] = (i - 1) / 2
            self.p[self.nodes[x][0]] = i
            self.switch(i, x)
            i = int((i - 1) / 2)
            x = int((i - 1) / 2)

        # print(self.nodes)
        # print(self.p)

    def inHeap(self, v):
        return self.p[v] < self.size


class Graph:

    def __init__(self, points):
        self.vertices = points
        self.graph = defaultdict(list)

    def addEdge(self, p1, p2, weight, p1_h, p2_h):

        newEdge1 = [p2, weight, p1_h]
        newEdge2 = [p1, weight, p2_h]
        self.graph[p1].insert(0, newEdge1)
        self.graph[p2].insert(0, newEdge2)

    def solution_path(self, parent, e, path):
        if parent[e] == -1:
            path.append(e)
            return
        self.solution_path(parent, parent[e], path)
        path.append(e)

    # def print_path_sol(self, distance, parent, end):
    #     print("\nstart --> {} \t\t{} \t\t\t\t".format(end, distance[end]))
    #     self.print_path(parent, end)

    def a_star(self, start, end):
        points = self.vertices
        distances = []
        parent = []
        minheap = minHeap()

        for point in range(points):
            distances.append(sys.maxsize)
            parent.append(-1)
            node = minheap.Node(point, distances[point])
            minheap.nodes.append(node)
            minheap.p.append(point)

        minheap.p[start] = start
        distances[start] = 0
        minheap.decreaseKey(start, distances[start])
        minheap.size = points

        while minheap.isEmpty() is False:
            newNode = minheap.heapPop()
            if newNode[0] == end:
                break

            x = newNode[0]

            for p in self.graph[x]:
                v = p[0]

                if minheap.inHeap(v) and distances[x] != sys.maxsize and (p[1] + p[2] + distances[x]) < distances[v]:
                    distances[v] = p[1] + p[2] + distances[x]
                    minheap.decreaseKey(v, distances[v])
                    parent[v] = x

        # print(minheap.nodes)
        # print(minheap.p)
        # print(distances)
        # self.print_path_sol(distances, parent, end)
        solution = []
        self.solution_path(parent, end, solution)
        return solution
