from manim import *

class Logo(Scene):
    def construct(self):

        v_left = Line(
            color = BLUE, start = np.array((-3.0, 3.0, 0.0)), end = np.array((-1.0, -1.0, 0.0)))

        v_right = Line(
            color = PURPLE, start = np.array((-1.0, -1.0, 0.0)), end = np.array((1.0, 3.0, 0.0)))

        a_right = Line(
            color = RED, start = np.array((1.0, 3.0, 0.0)), end = np.array((3.0, -1.0, 0.0)))
        
        a_cross = Line(
            color = RED, start = np.array((0.0, 1.0, 0.0)), end = np.array((2.0, 1.0, 0.0)))


        self.play(Create(v_left), time = 3)
        self.play(Create(v_right), time = 3)
        self.play(Create(a_right), Create(a_cross), time = 3)

        self.wait(10)



