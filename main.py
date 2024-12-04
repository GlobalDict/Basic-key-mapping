
# This script is attached to game Scene's active camera
# Nothing much here, just add overlay screen

from Range import *

class Game(types.KX_PythonComponent):
    args = {}
    
    def awake(self, args):
        logic.addScene("gui", 1)
    
    def start(self, args):
        pass
    
    def update(self):
        pass