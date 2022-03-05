from itertools import combinations
from manim import *

class ConvexHull(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range = [0, 10],  # step size determines num_decimal_places.
            y_range = [0, 10],
            x_length = 8,
            y_length = 6,
            axis_config={"include_numbers": True},
            tips = False
        )
        grid.shift(LEFT * 2)

        dot_list = []
        point_list = [(1, 7), (2, 6), (9, 2), (10, 8)]
        point_labels = ["p1", "p2", "p3", "p4"]

        self.add(grid)
        for i in range(len(point_list)):
            point = point_list[i]
            dot = Dot(grid.c2p(point[0], point[1]), color=PURPLE)
            dot_list.append(dot)

            dot_label = Text(point_labels[i], font_size=10).scale(1.25).next_to(
                            grid.c2p(point[0], point[1]))
            
            self.add(dot) # image version
            self.add(dot_label)
            # self.play(Create(dot), run_time = .25) # video version

        pairs_list = []
        pairs_text = VGroup()
        for pair in combinations(point_labels, 2):
            point_pair = Text(str(pair), font_size = 24)
            pairs_list.append(point_pair)
            pairs_text.add(point_pair)

        pairs_text.arrange(DOWN).shift(RIGHT * 5)
        self.add(pairs_text)

        """
        for pair of points:
            calculate the rise
            calculate the run
            calculate the equation of the line in the form Ax + By - C = 0

            above_line = 0
            below_line = 0
            for points:
                is_above = A*x + B*y
                if is_above > C:
                    above_line += 1
                elif is_above < C:
                    below_line += 1
        """

        convex_hull = []
        current_point = 0
        for i in range(len(point_list) - 1):
            for j in range(i + 1, len(point_list)):
                x1, y1 = point_list[i]
                x2, y2 = point_list[j]
                rise = y2 - y1
                run = x2 - x1
                c = (run * y1) - (rise * x1)

                if run == 0:
                    line = Line(Point(grid.c2p(x1, 0)), 
                                Point(grid.c2p(x1, 10)),
                                color = PURPLE)

                else:
                    min_x = (run/rise)*(-y1) + x1 
                    max_x = (run/rise)*(10-y1) + x1
                    if min_x > max_x:
                        min_x, max_x = max_x, min_x

                    line = grid.plot(
                        lambda x: (rise/run)*(x-x1) + y1,
                        x_range = [max(0, min_x), min(10, max_x)],
                        color = PURPLE
                    )

                pairs_list[current_point].set_color(PURPLE)
                self.play(Create(line))

                above_count = 0
                below_count = 0
                for k in range(len(point_list)):
                    current_x, current_y = point_list[k]
                    ax_and_by = (-1 * rise * current_x) + (run * current_y)

                    if ax_and_by < c:
                        dot_list[k].set_color(BLUE)
                        above_count += 1
                    elif ax_and_by > c:
                        dot_list[k].set_color(RED)
                        below_count += 1
                    else:
                        dot_list[k].set_color(PURPLE)

                if above_count == 0 or below_count == 0:
                    convex_hull.append(Line(dot_list[i], dot_list[j], color = PURPLE))
                    line.set_color(GREEN)

                self.wait(3)
                self.play(Uncreate(line))
                pairs_list[current_point].set_color(WHITE)
                current_point += 1
                for d in dot_list:
                    d.set_color(PURPLE)

        for line in convex_hull:
            self.play(Create(line))
        
        self.wait(5)

                



