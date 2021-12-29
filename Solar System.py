from ursina import *

app = Ursina()

class Sun(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'sphere'
        self.color = color.yellow
        self.scale_y = 2
        self.scale_x = 2
        self.scale_z = 2
    def update(self):
        self.x += held_keys['a'] * .1
        self.x -= held_keys['d'] * .1
        self.y += held_keys['left control'] * .1
        self.y -= held_keys['space'] * .1
        self.z += held_keys['s'] * .1
        self.z -= held_keys['w'] * .1
window.color = color.black
Sun = Sun()
EditorCamera()
app.run()
