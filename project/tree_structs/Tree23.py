from manim import *
from random import randrange

class TwoThreeTree(Scene):
    def construct(self):
        i, lst = 0, []
        while i < 10:
            r = randrange(0, 100)
            if r not in lst:
                lst.append(r)
                i += 1

        txt = Text("Create 23Tree From List: " + str(lst), font_size = 22).move_to(UP * 3)
        self.play(Write(txt))
        Tree23(self, lst)
        self.wait(2)

class Bubble():
    def __init__(self, scene, values, position):
        self.scene = scene
        self.vals = values
        self.text_size = 18
        self.move_to(position)
        self.draw()

    def get_top(self):
        return self.bubble.point_at_angle(PI/2)
    def get_bottom(self):
        return self.bubble.point_at_angle(3 * PI/2)
    def get_left(self):
        return self.bubble.point_at_angle(PI)

    def draw(self):
        self.scene.play(Create(self.bubble), Create(self.text))
    def undraw(self):
        self.scene.play(Uncreate(self.bubble), Uncreate(self.text))
    def move_to(self, position):
        self.pos = position
        self.bubble = Circle(.5, PURPLE).move_to(self.pos)
        self.text = Text(str(self.vals), font_size = self.text_size).move_to(self.pos)

    def add_connections(self, connections):
        self.scene.play(Create(VGroup(connections)))
    def rem_connections(self, connections):
        self.scene.play(Uncreate(VGroup(connections)))
    
    def update_text(self):
        self.scene.play(Uncreate(self.text))
        self.scene.wait(.5)
        self.text = Text(str(self.vals), font_size = self.text_size).move_to(self.pos)
        self.scene.play(Create(self.text))


class _Node23():
    def __init__(self, scene, key = None, trees = [], coords = np.array([0, -3, 0])):
        self.scene = scene
        self.keys = [key] if key is not None else []
        self.trees = list(trees)
        self.coords = coords
        self.bubble = Bubble(scene, self.keys, self.coords)
        self.draw_connections()
    
    def get_top(self):
        return self.bubble.get_top()
    def get_bottom(self):
        return self.bubble.get_bottom()
    def draw(self):
        self.bubble.draw()
        self.draw_connections()
    def draw_connections(self):
        self.connections = VGroup()
        for t in self.trees:
            self.connections.add(Line(self.get_bottom(), t.get_top(), color = PURPLE))
        self.bubble.add_connections(self.connections)
    def get_next_positions(self):
        c = (self.get_top() + self.get_bottom()) / 2
        x_val = c[0]

        if x_val > -.00001 and x_val < .00001:
            x1, x2 = (x_val - 7)/2, (x_val + 7)/2
            print((np.array([x1, c[1], 0]), np.array([x2, c[1], 0])))
            return (np.array([x1, c[1], 0]), np.array([x2, c[1], 0]))
        if x_val < 0:
            diff = min(abs((x_val - 7)/2 - x_val), abs(x_val/2 - x_val))
            print(x_val, x_val - diff, x_val + diff)
            print((np.array([x_val - diff, c[1], 0]), np.array([c[0] + diff, c[1], 0])))
            return (np.array([x_val - diff, c[1], 0]), np.array([x_val + diff, c[1], 0]))
        if x_val > 0:
            diff = min(abs((x_val + 7)/2 - x_val), abs(x_val/2 - x_val))
            print((np.array([x_val - diff, c[1], 0]), np.array([x_val + diff, c[1], 0])))
            return (np.array([x_val - diff, c[1], 0]), np.array([x_val + diff, c[1], 0]))

    def insert(self, item):
        if self.trees != []:
            i = self._key_scan(item)
            promoted_items = self.trees[i].insert(item)
            if promoted_items is not None:
                promoted_val, trees = promoted_items
                self.keys.insert(i, promoted_val)
                self.trees[i:i+1] = [trees[0], trees[1]]
                
                self.bubble.rem_connections(self.connections)
                self.bubble.update_text()
                self.draw_connections()

                # Deal with promoted items
                if len(self.keys) == 3:
                    p1, p2 = self.get_next_positions()
                    self.bubble.undraw()
                    self.bubble.rem_connections(self.connections)
                    return (self.keys[1], 
                    [_Node23(self.scene, self.keys[0], self.trees[0:2], p1), 
                    _Node23(self.scene, self.keys[2], self.trees[2:4], p2)])
        
        else:
            self.keys.append(item)
            self.keys.sort()
            self.bubble.update_text()
            if len(self.keys) == 3:
                # Deal with the case where the node is filled
                p1, p2 = self.get_next_positions()
                self.bubble.undraw()
                return (self.keys[1], 
                        [_Node23(self.scene, self.keys[0], coords = p1), 
                        _Node23(self.scene, self.keys[2], coords = p2)]) 
            return None
    
    def _key_scan(self, key):
        """Find the proper subtree for a key lookup"""
        i = 0
        while i < len(self.keys) and self.keys[i] < key:
            i += 1
        return i 


class Tree23():
    def __init__(self, scene, keys = []):
        self.coords = np.array([0, -3, 0])
        self.scene = scene
        self.tree = _Node23(self.scene, coords = self.coords)
        for k in keys:
            self.insert(k)

    def insert(self, item):
        """Returns None if item is inserted in the tree
        Returns (rootkey, [leftTree, rightTree])"""
        result = self.tree.insert(item)
        if result is not None:
            promoted_val, trees = result
            self.coords = self.coords + np.array([0, 1.5, 0])
            self.tree = _Node23(self.scene, promoted_val, trees, self.coords)