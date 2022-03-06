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