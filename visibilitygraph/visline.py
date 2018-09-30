import math


def onSeg(pt1, pt2, pt3):
    if (pt2[0] <= max(pt1[0], pt3[0]) and pt2[0] >= min(pt1[0], pt3[0]) and
            pt2[1] <= max(pt1[1], pt3[1]) and pt2[1] >= min(pt1[1], pt3[1])):
        return True
    return False


def orient(pt1, pt2, pt3):
    o = ((pt2[1] - pt1[1]) * (pt3[0] - pt2[0]) - (pt2[0] - pt1[0]) * (pt3[1] - pt2[1]))

    if(o == 0):
        return 0
    elif o > 0:
        return 1
    else:
        return 2


def intersection(pt1, pt2, pt3, pt4):
    o1 = orient(pt1, pt2, pt3)
    o2 = orient(pt1, pt2, pt4)
    o3 = orient(pt3, pt4, pt1)
    o4 = orient(pt3, pt4, pt2)

    if (o1 != o2 and o3 != o4):
        return True

    if (o1 == 0 and onSeg(pt1, pt3, pt2)):
        return True

    if (o2 == 0 and onSeg(pt1, pt4, pt2)):
        return True

    if (o3 == 0 and onSeg(pt3, pt1, pt4)):
        return True

    if (o4 == 0 and onSeg(pt3, pt2, pt4)):
        return True

    return False
