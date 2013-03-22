
import sys
import string
from PySFML import sf
#from Drawable_Objects import Drawable_Toolbox,Drawable_FunctionSet
from LevelEditor_Objects import LevelEditor_Objects,Drawable_Scenario,Drawable_Box,GenerarXML
from Application import Application

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
        self.deleteicon = None
        self.idbox = 1
        self.xml = GenerarXML()
       # self.toolbox = Drawable_Toolbox()
        self.tools = LevelEditor_Objects()
        self.di = None
        
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
        self.addstack.Resize(150,75)
        self.addstack.SetCenter(0, 0)
        self.addstack.SetPosition(0,0)

    def DefinirdeleteStackBoton(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_deletestack.png")
        self.deletestack = sf.Sprite(image)
        self.deletestack.Resize(150,75)
        self.deletestack.SetCenter(0, 0)
        self.deletestack.SetPosition(0,85)

    def DefinirX(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/X.png")
        self.deletestackX = sf.Sprite(image)
        self.deletestackX.Resize(50,50)
        self.deletestackX.SetCenter(0, 0)
        self.deletestackX.SetPosition(95,85)
        return self.deletestackX

    def DefinirSaveBoton(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_save.png")
        self.save = sf.Sprite(image)
        self.save.Resize(150,75)
        self.save.SetCenter(0, 0)
        self.save.SetPosition(1050,0)
        
    def BotonHovered(self, x, y):
        if(x>0 and x<150 and y>0 and y<75):
            return "ADDSTACK"
        if(x>0 and x<150 and y>85 and y<160):
            return "DELETESTACK"
        if(x>1050 and x<1200 and y>0 and y<75):
            return "SAVE"
        
        if( x>140 and x<180):
            return ["goal",0]
        if( x>190 and x<230 ):
            return ["goal",1]
        if( x>240 and x<280 ):
            return ["goal",2]
        if( x>290 and x<330 ):
            return ["goal",3]
        if( x>340 and x<380 ):
            return ["goal",4]
        if( x>390 and x<430 ):
            return ["goal",5]
        if( x>340 and x<480 ):
            return ["goal",6]
        if( x>490 and x<530 ):
            return ["goal",7]
        
        if( x>660 and x<705 ):
            return ["scene",0]
        if( x>715 and x<760 ):
            return ["scene",1]
        if( x>770 and x<815 ):
            return ["scene",2]
        if( x>825 and x<870 ):
            return ["scene",3]
        if( x>885 and x<930 ):
            return ["scene",4]
        if( x>940 and x<985 ):
            return ["scene",5]
        if( x>995 and x<1040 ):
            return ["scene",6]
        if( x>1050 and x<1095 ):
            return ["scene",7]
        
    def Pintar(self):
        self.window.Draw(self.Fondo)
        self.window.Draw(self.addstack)       
        self.window.Draw(self.deletestack)
        self.window.Draw(self.save)
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
        self.DefinirdeleteStackBoton()
        self.DefiniraddStackBoton()
        self.DefinirSaveBoton()
        
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
                                print("entro aqui y no debe")
                                self.temp = self.DuplicateBox(ins)
                            else:
                                self.temp.SetImage(self.GetImage(ins))
                                

                            self.dragging_box = True
                    
                        else:
                            self.goal.Clear()
                            self.scenario.Clear()
                        
                       
                    else:
                    #    cual = self.BotonHovered(x,y)
                       
                                    
                        if boton == "ADDSTACK":
                            self.scenario.addStack()
                            self.goal.addStack()
                        if boton == "DELETESTACK":
                            
                            self.deleteicon = True
                            clickstack = False
                            print("por aki 1 .....")
                        if boton == "SAVE":
                            self.xml.Generar(self.scenario,self.goal)
                        if self.deleteicon == True:
                            print("por aki 2 .....")

                            if boton != None:
                                print("por aki3 .....")
                                if boton != "ADDSTACK" and boton != "DELETESTACK" and boton !="SAVE":
                                    clickstack = True
                                #    print(cual)
                                
                            if clickstack == True:
                                print("por aki 4 .....")
                                self.scenario.deleteStack(boton[1])
                                self.goal.deleteStack(boton[1])
                                self.deleteicon = False
                        else:
                            if boton is not None:
                                if boton != "ADDSTACK" and boton != "DELETESTACK" and boton != "SAVE":
                                    if boton[0] == "scene":
                                        ift=self.scenario.BoxClicked(x,y,boton[1])
                                    if boton[0] == "goal":
                                        ift=self.goal.BoxClicked(x,y,boton[1])
                                    #self.temp = self.goal.BoxClicked(x,y,boton[1])[0]
                                    self.temp = ift[0]
                                    #ins = self.goal.BoxClicked(x,y,boton[1])[1]
                                    ins = ift[1]
                                    self.dragging_box = True
                           
                                    

                                
                if self.Evento.Type == sf.Event.MouseButtonReleased:

                    
                    
                    if boton is not None:
                        print("aqui")
                        if boton[0] == "goal":
                            if ins is not None:
                               
                                self.goal.PlaceBox(boton[1],ins)
                                #self.idbox+=1
                                         
                        if boton[0] == "scene":
                            if ins is not None:
                                self.scenario.PlaceBox(boton[1],ins)
                    Application.putOnDeleteList(self.temp)            
                    self.temp = None
                    self.dragging_box = False            
                    
                
                    

            self.scenario.Update(frameTime)
            #self.goal.Update(frameTime)              
            self.window.Clear(self.blanco)
            
            self.Pintar()
            self.tools.Pintar(self.window)
            self.scenario.Pintar(self.window)
            self.goal.Pintar(self.window)
            
            if self.dragging_box:
                self.temp.SetPosition(x - 22, y - 22)
                self.window.Draw(self.temp)
                
            if self.deleteicon:
                if self.di != None:
                    Application.putOnDeleteList(self.di)
                self.di = self.DefinirX()
                self.di.SetPosition(x-22,y-22)
               
                self.window.Draw(self.di)
               # 
           # else:
              #  self.DefinirdeleteStackBoton()
                #self.window.Draw(self.deletestack)
            self.window.Display()

if __name__ == "__main__":
    ven = Level_Editor()
    ven.Update()
   
