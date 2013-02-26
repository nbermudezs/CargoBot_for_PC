import sys
import string
from PySFML import sf
#from Drawable_Objects import Drawable_Toolbox,Drawable_FunctionSet
from LevelEditor_Objects import LevelEditor_Objects,Drawable_Scenario,Drawable_Box

class Level_Editor: 
    Evento = None
    window = None
    Fondo = None
    DIRECTORIO = "images/"
	
    def __init__(self):
        self.width = 1200
        self.heigth = 700
        self.blanco = sf.Color(250, 250, 250)
        self.negro =  sf.Color(0, 0, 0)
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - LETS START")
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)
        self.temp = None
        self.box_name = None
        self.ins= None
        self.dragging_box = None
        self.idbox = 1
       # self.toolbox = Drawable_Toolbox()
        self.tools = LevelEditor_Objects()
       # self.function_set = Drawable_FunctionSet()
        self.scenario = Drawable_Scenario(590, 187, 1200, 700, False)
        self.goal = Drawable_Scenario(77, 187, 628, 700, True)
        
    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/leveleditor.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200, 700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)

    def DefiniraddStackBoton(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_addstack.png")
        self.addstack = sf.Sprite(image)
        self.addstack.Resize(200,100)
        self.addstack.SetCenter(0, 0)
        self.addstack.SetPosition(0,70)


    def BotonHovered(self, x, y):
        if(x>0 and x<200 and y>70 and y<170):
            return "ADDSTACK"
            
    def Pintar(self):
        self.window.Draw(self.Fondo)
        self.window.Draw(self.addstack)       
        
    def DuplicateBox(self, box):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/box_"+box+".png")
        temp = sf.Sprite(image)
        temp.Resize(40, 40)
        temp.SetCenter(0, 0)
        temp.SetPosition(11, 569)

        
        return temp

    def GetImage(self, box):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/box_"+box+".png")
        return image

    def SetDraggingBox(self, box):
        self.box_name = self.ins
        if self.temp == None:
            if self.ins != None:
                self.temp = self.DuplicateBox(box)
        else:
            self.temp.SetImage(self.GetImage(box))

        self.dragging_box = True

    
        
    
    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefiniraddStackBoton()
        
        q = False
        
        while not q:
            x = input.GetMouseX()
            y = input.GetMouseY()
            boton = self.BotonHovered(x, y)
            frameTime = self.window.GetFrameTime()        
            while self.window.GetEvent(self.Evento):
                print self.Evento.Type
                if self.Evento.Type == sf.Event.Closed:
                    self.window.Close()

                if self.Evento.Type == sf.Event.MouseButtonPressed:
                    self.box_name = self.tools.InstructionToolboxClicked(x, y)
                    
                    ins = self.box_name
                    print(str(x))
                    print(str(y))
                    if ins != None:
                        if ins != "INS_CLEAR":
                            if self.temp == None:
                               
                                self.temp = self.DuplicateBox(ins)
                            else:
                                self.temp.SetImage(self.GetImage(ins))
                                

                            self.dragging_box = True
                    
                        else:
                            pass
                       
                    else:
                       
                        if boton == "ADDSTACK":
                            self.scenario.addStack()
                            self.goal.addStack()
                        else:
                           pass 
                            
                            
                if self.Evento.Type == sf.Event.MouseButtonReleased:


                    if ins is not None:
                        self.scenario.PlaceBox([self.idbox,ins])
                    
                   # self.temp = None                    
                    self.dragging_box = False

           # self.scenario.Update(frameTime)              
            self.window.Clear(self.blanco)
            
            self.Pintar()
            self.tools.Pintar(self.window)
            self.scenario.Pintar(self.window)
            self.goal.Pintar(self.window)
            if self.dragging_box:
                self.temp.SetPosition(x - 22, y - 22)
                self.window.Draw(self.temp)
            
            self.window.Display()

if __name__ == "__main__":
    ven = Level_Editor()
    ven.Update() 

