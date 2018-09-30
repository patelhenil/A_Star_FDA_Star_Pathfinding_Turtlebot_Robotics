from graph import Point, Edge, Polygon, generate_visible_edges
from visline import intersection
from astar_vis import Graph, minHeap


def main():

    point1 = Point(-1, -1, 1)
    point2 = Point(-5, -1, 1)
    point3 = Point(-5, 2, 1)
    point4 = Point(-3, 2, 1)

    point5 = Point(-2, 2, 2)
    point6 = Point(2, 2, 2)
    point7 = Point(2, -4, 2)

    point8 = Point(-1, -1.25, 3)
    point9 = Point(-5, -2.5, 3)
    point10 = Point(-5, -5, 3)
    point11 = Point(1.2, -5, 3)
    point12 = Point(1.2, -4, 3)

    s1 = []
    s2 = []
    s3 = []

    s1.append(point1)
    s1.append(point2)
    s1.append(point3)
    s1.append(point4)

    s2.append(point5)
    s2.append(point6)
    s2.append(point7)

    s3.append(point8)
    s3.append(point9)
    s3.append(point10)
    s3.append(point11)
    s3.append(point12)

    Polylist = []
    poly1 = Polygon(s1)
    poly2 = Polygon(s2)
    poly3 = Polygon(s3)

    Polylist.append(poly1)
    Polylist.append(poly2)
    Polylist.append(poly3)

    start = Point(-1, -1.75, 0)
    end = Point(-5, -1.75, 0)
    gtuple = generate_visible_edges(Polylist, start, end)
    visibility_graph = Graph(len(gtuple[1]))

    for edge in gtuple[0]:
        dist = edge.gx()
        # print(edge, dist)
        visibility_graph.addEdge(edge.p1.point_id, edge.p2.point_id, dist,
                                 edge.p1.point_distance(end), edge.p2.point_distance(end))

    # for x, y in visibility_graph.graph.items():
    #     print(x, y)

    path = visibility_graph.a_star(start.point_id, end.point_id)
    solution = []
    for p in path:
        for i in gtuple[1]:
            if p == i.point_id:
                solution.append(i)
    print(solution)


if __name__ == "__main__":
    main()
