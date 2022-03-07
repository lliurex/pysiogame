# -*- coding: utf-8 -*-
import math


def rotate_point(point, centre, angle):
    """ Rotates a point around another point by a number of degrees (anticlockwise)
    :param point: point coordinates - 2 element list
    :param centre: centre of rotation coordinates - 2 element list
    :param angle: rotate by the given angle
    :return: a rotated point - 2 element list
    """
    # convert angle to radians
    angle = math.radians(angle)

    pt = [0, 0]

    # translate the rotation point to the origin
    pt[0] = point[0] - centre[0]
    pt[1] = point[1] - centre[1]

    # calculate the new coordinates after rotation
    res = [int(round(pt[0] * math.cos(angle) - pt[1] * math.sin(angle))),
           int(round(pt[1] * math.cos(angle) + pt[0] * math.sin(angle)))]

    # cancel translation
    res[0] += centre[0]
    res[1] += centre[1]

    return res


def rotate_points(points, centre, angle):
    """ Rotates a list of points around another point by a number of degrees (anticlockwise)
    :param points: a list of 2 element lists containing initial coordinates of individual points
    :param centre: a list of 2 elements containing a coordinates of the centre of rotation
    :param angle: the angle by which the points are to be rotated in degrees
    :return: a list of rotated points about a centre point
    """
    rotated_points = []
    for point in points:
        rotated_points.append(rotate_point(point, centre, angle))

    print(rotated_points)
    return rotated_points


def test_rotate_points():
    assert rotate_points([[1, 0], [0, 1]], [0, 0], 90) == [[0, 1], [-1, 0]]
    assert rotate_points([[1, 0], [0, 1]], [1, 1], 90) == [[2, 1], [1, 0]]
    assert rotate_points([[1, 1], [-2, -2]], [-1, -1], 90) == [[-3, 1], [0, -2]]


test_rotate_points()
