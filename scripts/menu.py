from scripts.obj import Obj
from scripts.scene import Scene

class Menu(Scene):
    def __init__(self):

        super().__init__()
        self.bg = Obj("assets/start.wav", [self.all_sprites])