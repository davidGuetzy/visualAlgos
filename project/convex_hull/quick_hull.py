from manim import *
from plot_helpers import create_points_with_labels

class ConvexHull(Scene):
    def construct(self):
        self.upper_hull = []
        # the location of the ticks depends on the x_range and y_range.
        self.grid = Axes(
            x_range = [0, 10],  # step size determines num_decimal_places.
            y_range = [0, 10],
            x_length = 8,
            y_length = 6,
            axis_config={"include_numbers": True},
            tips = False
        )
        self.grid.shift(LEFT * 2)
        point_list = [(1, 4), (3, 6), (5, 9), (10, 8)]
        point_list.sort() # Assert that the point_list is sorted
        point_labels = ["p1", "p2", "p3", "p4"]
        dot_list = create_points_with_labels(self.grid, point_list, point_labels)

        self.play(Create(self.grid))
        for dot, label in dot_list:
            self.play(Create(dot), Create(label), run_time = .5)

        self.find_upper_hull_segment(point_list[0], point_list[-1], point_list[1: -1])

    def find_upper_hull_segment(self, left_point, right_point, possible_points):
        """Take a line and set of points and determine points in the upper hull"""
        max_angle = 0
        max_area = 0
        max_point = None
        max_triangle = None
        x1, y1 = left_point
        x2, y2 = right_point
        
        midline = Line(self.grid.c2p(x1, y1, 0), self.grid.c2p(x2, y2, 0), color = PURPLE)
        self.play(Create(midline))
        self.wait(2)

        for x3, y3 in possible_points:
            # Point can only be in the upper hull if it above the line
            if y3 > y1 or y3 > y2:
                candidate_area = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3
                candidate_triangle = Polygon(self.grid.c2p(x1, y1, 0), 
                                            self.grid.c2p(x2, y2, 0), 
                                            self.grid.c2p(x3, y3, 0))
                candidate_triangle.set_color(BLUE)
                candidate_triangle.set_fill(BLUE, opacity = .5)
                self.play(Create(candidate_triangle))
                self.wait(2)
                if max_area > candidate_area:
                    self.play(Uncreate(candidate_triangle))
                elif candidate_area > max_area:
                    max_angle, max_area, max_triangle = self.replace_max_triangle_with_candidate(
                        [candidate_area, candidate_triangle, 
                        (Point(self.grid.c2p(x1, y1, 0)), 
                        Point(self.grid.c2p(y2, y2, 0)), 
                        Point(self.grid.c2p(x3, y3, 0)))],
                        max_triangle)
                    max_point = (x3, y3)
                else:
                    candidate_angle = abs(Line(Point(self.grid.c2p(x3, y3, 0)), Point(self.grid.c2p(x1, y1, 0))).get_angle() 
                                        - Line(Point(self.grid.c2p(x3, y3, 0)), Point(self.grid.c2p(x2, y2, 0))).get_angle())
                    if max_angle > candidate_angle:
                        self.play(Uncreate(candidate_triangle))
                    else:
                        max_angle, max_area, max_triangle = self.replace_max_triangle_with_candidate(
                            [candidate_area, candidate_triangle, 
                            (Point(self.grid.c2p(x1, y1, 0)), 
                            Point(self.grid.c2p(y2, y2, 0)), 
                            Point(self.grid.c2p(x3, y3, 0)))],
                            max_triangle)
                        max_point = (x3, y3)
        
        if max_point is not None:
            self.play(Uncreate(max_triangle), Uncreate(midline))
            self.find_upper_hull_segment(left_point, max_point,
                possible_points[:possible_points.index(max_point)])
            self.upper_hull.append(Point(self.grid.c2p(x3, y3, 0)))
            self.find_upper_hull_segment(max_point, right_point,
                possible_points[possible_points.index(max_point) + 1:])
    
    def replace_max_triangle_with_candidate(self, candidate_info, max_triangle):
        candidate_area, candidate_triangle, candidate_vertices = candidate_info
        p1, p2, p3 = candidate_vertices
        if max_triangle is not None:
            self.play(Uncreate(max_triangle))
        
        max_angle = abs(Line(p3, p1).get_angle() - Line(p3, p2).get_angle())
        max_triangle = candidate_triangle.copy()
        max_triangle.set_color(PURPLE)
        max_triangle.set_fill(PURPLE)
        self.play(
            Create(max_triangle),
            Uncreate(candidate_triangle), run_time = .5
        )

        return [max_angle, candidate_area, max_triangle]
            

                
                


                
        
        


