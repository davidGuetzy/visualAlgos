from lib2to3.pgen2.token import LEFTSHIFT, LEFTSHIFTEQUAL
from manim import *

class ConvexHull(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range = [0, 10],  # step size determines num_decimal_places.
            y_range = [0, 10],
            x_length = 7,
            y_length = 6,
            axis_config={"include_numbers": True},
            tips = False
        )
        grid.shift(np.array((-2.5, 0.0, 0.0)))
        
        point_list = [(1, 7), (2, 2), (2, 6), (4, 3),
            (5, 9), (6, 6), (7, 4), (8, 3), (9, 2), (10, 8)]
        
        dot_list = [
            Dot(grid.c2p(1, 7), color=PURPLE),
            Dot(grid.c2p(2, 2), color=PURPLE),
            Dot(grid.c2p(2, 6), color=PURPLE),
            Dot(grid.c2p(4, 3), color=PURPLE),
            Dot(grid.c2p(5, 9), color=PURPLE),
            Dot(grid.c2p(6, 6), color=PURPLE),
            Dot(grid.c2p(7, 4), color=PURPLE),
            Dot(grid.c2p(8, 3), color=PURPLE),
            Dot(grid.c2p(9, 2), color=PURPLE),
            Dot(grid.c2p(10, 8), color=PURPLE)
        ]

        self.add(grid)
        for dot in dot_list:
            self.add(dot) # image version
            # self.play(Create(dot), run_time = .25) # video version

        ALGO_FONT_SIZE = 28
        line1 = Tex(r'$P = \{p_1, p_2, p_3, ... p_n\}$',
                    font_size = ALGO_FONT_SIZE)
        line2 = Tex('for ', r'$i \leftarrow 1$', ' to ', r'$n - 1$', 
                    font_size = ALGO_FONT_SIZE)
        line3 = Tex(r'$\text{ for } j \leftarrow i \text{ to } n$', 
                    font_size = ALGO_FONT_SIZE)
        line4 = Tex('a ', r'$\leftarrow y_2 - y_1$',
                    font_size = ALGO_FONT_SIZE).shift(RIGHT)
        line5 = Tex('b ', r'$\leftarrow x_2 - x_1$',
                    font_size = ALGO_FONT_SIZE)
        line6 = Tex('line ', r'$\leftarrow (a, -b, by - ax)$',
                    font_size = ALGO_FONT_SIZE)
        
        brute_force_algo = VGroup(line1, line2, line3, line4, line5, line6).arrange(
                            DOWN, center=False, aligned_edge = LEFT)
        
        brute_force_algo.shift(np.array((3.5, 3, 0)))
        line3.shift(.5 * RIGHT)
        line4.shift(RIGHT)
        line5.shift(RIGHT)
        line6.shift(RIGHT)
        self.add(brute_force_algo)

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

        a1 = (1, 7)
        b1 = (7, 4)

        a = Dot(grid.c2p(1, 7), color=PURPLE)
        b = Dot(grid.c2p(7, 4), color=PURPLE)
        a_center = a.get_center()
        b_center = b.get_center()

        rise = b1[1] - a1[1]
        run = b1[0] - a1[0]
        number = run * a1[1] - rise * a1[0] 

        line1 = Line(a, b, color = BLUE)


        print(rise, run)
        for point in point_list:
            argh = rise * point[0] - run * point[1]
            print(argh)
            if argh > number:
                dot.set_color(RED)
            else:
                dot.set_color(GREEN)

        line1.set_length(7)
        self.add(line1)
                



