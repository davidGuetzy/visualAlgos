from manim import *

class CoordSysExample(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[0, 10],  # step size determines num_decimal_places.
            y_range=[0, 10],
            x_length=9,
            y_length=6,
            tips = False
        )

        dot_list = []
        for i in range(10):
            for j in range(10):
                # a dot with respect to the axes
                dot_axes = Dot(grid.coords_to_point(2, 2), color=PURPLE)
                dot_list.append(dot_axes)

        
        self.add(grid)
        for dot in dot_list:
            self.play(Create(dot))


