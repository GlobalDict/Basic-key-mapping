# Global Dict
# This script is attached to the GUI Scene's active camera
# Basic, that is to say not perfect !

from Range import *

class keyMap(types.KX_PythonComponent):
    args = {}
    
    def awake(self, args):
        self.gameScene = logic.getSceneList()["game"]
        self.objects = self.gameScene.objects
        
        self.thisScene = logic.getSceneList()["gui"]
        self.obj = self.thisScene.objects
        self.clickMe = self.obj["clickMe"]
        self.enter = self.obj["enter"]
        
        self.player = self.objects["Cube"]
        self.keyboard = logic.keyboard.inputs
    
    def start(self, args):
        pass
    
    def update(self):
        
        # Check if the script owner (self.object) is active
        if self.object["active"] == True:
            
            # Hide the enter button from the screen
            self.enter.visible = False
            
            # define your custom key. use upper() because Range events are all Upper case
            self.customKey = str(self.obj["key"].text + "KEY").upper()
            
            # set your custom key to be the forward key
            self.forwardKey = self.keyboard[events.__dict__[self.customKey]]
            
            # Use your forward key
            if self.forwardKey.active:
                self.player.applyMovement([0,0.1,0])
                
        # Get mouse cursor position on the screen
        pos = logic.mouse.position
        
        # Get the object pointed by the mouse cursor within the distance of 15 from camera world position
        over = self.object.getScreenRay(pos[0], pos[1], 15)
        
        # 1st check if the mouse cursor is pointing at any button to avoide errors
        if over is not None:
            
            # New button scale
            s = 1.1
            
            # If the mouse is hovering over click me button
            if over == self.clickMe:
                # Rescale the button
                self.clickMe.worldScale = (s,s,s)
                
                # If button clicked
                if logic.mouse.inputs[events.LEFTMOUSE].activated:
                    # Deactivate camera state to avoid the game from crushing if player types an invalid key
                    self.object["active"] = False
                    
                    # Activate key object to allow it to take some user input from the keyboard
                    self.obj["key"]["active"] = True
                    
                    # Show enter button for the player to be able to confirm their key
                    self.enter.visible = True
                    
                    # Delete the default key 
                    self.obj["key"].text = ""
                
            # If mouse cursor is hovering over enter button
            if over == self.enter:
                # Rescale
                self.enter.worldScale = (s,s,s)
                
                # If button clicked
                if logic.mouse.inputs[events.LEFTMOUSE].activated:
                    
                    # Check if the user did not type a number.
                    # If they type a number, the default forward key will be restored
                    if self.obj["key"].text.isdigit():
                        self.obj["key"].text = "W"
                    
                    # Check if the user inputs more than 1 keys and restore the default forward key
                    if len(self.obj["key"].text) >1:
                        self.obj["key"].text = "W"
                        
                    # If user did not type any key, restore the default forward key
                    if self.obj["key"].text == "" :
                        self.obj["key"].text = "W"
                        
                    # Deactivate key key object. It will not take any user input
                    self.obj["key"]["active"] = False
                    
                    # Activate camera state
                    self.object["active"] = True
                    
                    # Hide the enter button from the screen again
                    self.enter.visible = False
                    
        # Resize buttons if not hovered
        else:
            self.clickMe.worldScale = (1,1,1)
            self.enter.worldScale = (1,1,1)
            
            
        