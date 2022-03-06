# plot_helpers.py
# This file contains some helper functions for manim plots

from manim import *

def create_points_with_labels(grid, point_list, label_list):
    """Given a list of tuples and string labels,
    Construct a list of dot objects with the labels on the specified grid"""
    dot_list = []
    for i in range(len(point_list)):
            point = point_list[i]
            dot = Dot(grid.c2p(point[0], point[1]), color=PURPLE)
            label = (Text(label_list[i], font_size=10).scale(1.25).next_to(
                            grid.c2p(point[0], point[1])))
            dot_list.append((dot, label))
            
    return dot_list

def is_point_above_line(line, point):
    """Given a line and point mobject,
    If point is above line return True, else return False"""
    end1 = line.get_points_defining_boundary()[0]
    x1, y1, z1 = end1
    slope = line.get_slope()
    px, py, pz = point.get_all_points()[0]
    
    return py > slope*(px-x1) + y1

def is_point_below_line(line, point):
    """Given a line and point mobject,
    If point is below line return True, else return False"""
    end1 = line.get_points_defining_boundary()[0]
    x1, y1, z1 = end1
    slope = line.get_slope()
    px, py, pz = point.get_all_points()[0]

    return py < slope*(px-x1) + y1