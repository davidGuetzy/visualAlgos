from manim import *

class CreateLogo(Scene):
    def construct(self):
        letter_size = 15

        v_left = Line(
            color = BLUE, 
            start = np.array((-3.0, 3.0, 0.0)), 
            end = np.array((-1.0, -1.0, 0.0)), 
            stroke_width = letter_size)

        v_right = Line(
            color = PURPLE, 
            start = np.array((-1.0, -1.0, 0.0)), 
            end = np.array((1.0, 3.0, 0.0)),
            stroke_width = letter_size)

        a_right = Line(
            color = RED, 
            start = np.array((1.0, 3.0, 0.0)), 
            end = np.array((3.0, -1.0, 0.0)),
            stroke_width = letter_size)
        
        a_cross = Line(
            color = RED, 
            start = np.array((0.0, 1.0, 0.0)), 
            end = np.array((2.0, 1.0, 0.0)),
            stroke_width = letter_size)

        name = Text("Visualizing Algorithms", color = WHITE).shift(DOWN * 2)
        border = RoundedRectangle(.5, height = 6, width = 9).shift(UP * .5)
        
        title = Text("Title of this video", color = WHITE, font_size = 48).shift(DOWN * 2)
        
        self.play(Create(v_left), run_time = 2)
        self.play(Create(v_right), run_time = 2)
        self.play(Create(a_right), Create(a_cross), run_time = 2)
        self.play(Write(name), Create(border), run_time = 5)
        self.wait(2)
        self.play(ReplacementTransform(name, title), run_time = 3)
        self.wait(5)

        # uncommenting this will give you a png
        # self.add(v_left, v_right, a_right, a_cross, name, border)



