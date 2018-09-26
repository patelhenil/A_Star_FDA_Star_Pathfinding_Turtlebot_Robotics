# -*- coding: utf-8 -*-
import math
import copy


# square root of 2 for diagonal distance
SQRT2 = math.sqrt(2)


def backtrace(node):
    """
    Backtrace according to the parent records and return the path.
    (including both start and end nodes)
    """
    path = [(node.x, node.y)]
    while node.parent:
        node = node.parent
        path.append((node.x, node.y))
    path.reverse()
    return path


def bresenham(coords_a, coords_b):
    '''
    Given the start and end coordinates, return all the coordinates lying
    on the line formed by these coordinates, based on Bresenham's algorithm.
    http://en.wikipedia.org/wiki/Bresenham's_line_algorithm#Simplification
    '''
    line = []
    x0, y0 = coords_a
    x1, y1 = coords_b
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        line += [[x0, y0]]
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy

    return line
