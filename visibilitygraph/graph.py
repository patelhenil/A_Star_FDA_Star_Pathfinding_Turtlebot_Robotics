from visline import intersection
from collections import defaultdict
import math


class Point:

    num_of_points = 0

    def __init__(self, x, y, poly_id):
        self.co = (x, y)
        self.id = poly_id
        self.point_id = Point.num_of_points

        Point.num_of_points += 1

    def __repr__(self):
        return "{}".format(self.co)

    def point_distance(self, endpoint):
        return math.hypot(endpoint.co[1] - self.co[1], endpoint.co[0] - self.co[0])


class Edge:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1.id != p2.id:
            self.eid = -1
        else:
            self.eid = p1.id

    def __repr__(self):
        return "{}-->{}".format(self.p1, self.p2)

    def __eq__(self, other):
        return (self.p1.co == other.p1.co or self.p1.co == other.p2.co) and (self.p2.co == other.p1.co or self.p2.co == other.p2.co)

    def intersects(self, edge):
        if self == edge:
            return False
        elif (self.p1.co == edge.p1.co or self.p1.co == edge.p2.co) or (self.p2.co == edge.p1.co or self.p2.co == edge.p2.co):
            return False
        else:
            return intersection(self.p1.co, self.p2.co, edge.p1.co, edge.p2.co)

    def gx(self):
        return math.hypot(self.p2.co[1] - self.p1.co[1], self.p2.co[0] - self.p1.co[0])


class Polygon:
    def __init__(self, Points):
        self.points = Points
        self.edges = []
        for i in range(len(Points)):
            edge = Edge(Points[i], Points[(i + 1) % len(Points)])
            self.edges.append(edge)

    def __repr__(self):
        return "{}".format(self.edges)


def generate_visible_edges(Polygonlist, start, end):
    combined_points = [start, end]
    combined_edges = []
    visible_edges = []
    for poly in Polygonlist:
        combined_points += poly.points
        combined_edges += poly.edges

    counter = 0
    for point in combined_points:
        for p in combined_points[counter + 1:]:
            edge = Edge(point, p)
            if edge in combined_edges:
                # print(edge, "Part of polygon")
                visible_edges.append(edge)
            else:
                bool = True
                for nedge in combined_edges:
                    if edge.eid == nedge.eid:
                        # print(edge, "Invalid Inner edge")
                        bool = False
                        break
                    elif edge.intersects(nedge):
                        # print(edge, nedge, "Intersects Polygonal Edge")
                        bool = False
                        break
                if bool:
                    visible_edges.append(edge)
        counter += 1
    return (visible_edges, combined_points)
