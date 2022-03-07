# text_helpers.py
# This file contains some helper functions for manim text

from manim import * 

def change_text_in_this_mobject(old_text, newInfo):
    center = old_text.get_center()
    size = old_text._font_size

    newText = Text(newInfo, font_size = size)
    newText.shift(center)

    return newText
    