import sys
import string
from PySFML import sf
from Application import Application
from Icon import Icon
from Drawable_Objects import Drawable_Toolbox, Drawable_FunctionSet, Drawable_Scenario, Drawable_Slider, Drawable_Message

class Game_Window: 
    Fondo = None
    DIRECTORIO = "images/"
	
    def __init__(self, prevScreen, puzzle_number):
        self.puzzle_number = puzzle_number
        self.width = 1200
        self.heigth = 700
        self.blanco = sf.Color(250, 250, 250)
        self.negro =  sf.Color(0, 0, 0)
        name = Application.username
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "DRAG BOX - LETS PLAY " + name, sf.Style.Close)
        self.window.SetIcon(16,16,Icon.window_icon())
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)
        self.backScreen = prevScreen
        self.sonidos = None
        self.temp = None
        self.dragging_instruction = False
        self.playing = False
        self.playingStepByStep = False
        self.instruction_name = None
        self.function_set = Drawable_FunctionSet()
        self.slider = Drawable_Slider(249, 98, 505, 143, 50)

        self.toolbox = Drawable_Toolbox()
        self.goal = Drawable_Scenario(77, 461, 511, 700, prevScreen, str(puzzle_number), True)
        self.working_area = Drawable_Scenario(529, 87, 1200, 700, prevScreen, str(puzzle_number), False)
        self.working_area.goal = self.goal
        self.message = None
        Application.setActiveWindow(self)
        
    def DefinirFondo(self):
        self.Fondo = Application.createSfSprite(self.DIRECTORIO+"bgs/TBG.png", 0, 0, 1200, 700)
        
        font = sf.Font()
        font = sf.Font.GetDefaultFont()
        #font.LoadFromFile('my_downloaded_font.ttf', 50)
        self.tittle = sf.String("LEVEL: " + self.backScreen + ", PUZZLE " + str(self.puzzle_number) + "(" + Application.username + ")", font)
        color = sf.Color(0, 0, 0)
        rect = self.tittle.GetRect()
        self.tittle.SetColor(color)
        self.tittle.SetCenter(0,0)        
        self.tittle.SetSize(35)
        self.tittle.SetPosition((1200 - rect.GetWidth())/2, 15)

        self.delimiter = Application.createSfSprite(self.DIRECTORIO+"gameplay/delimiter.png", 0, rect.GetHeight() + 47, 1200, 10)

    def BotonHome(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def SetMessage(self, msg):
        self.message = msg

    def BotonBack(self):
        nuevaVentana = None
        if self.backScreen == "TUTORIAL":
            from Tutorial_Puzzles import Tutorial_Puzzles
            nuevaVentana = Tutorial_Puzzles()
        if self.backScreen == "EASY":
            from Easy_Puzzles import Easy_Puzzles
            nuevaVentana = Easy_Puzzles()
        if self.backScreen == "GODMODE":
            from Misc_Puzzles import Misc_Puzzles
            nuevaVentana = Misc_Puzzles()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonPlayStop(self):
        self.playingStepByStep = False
        image = sf.Image()
        if self.playing:
            self.working_area.DetenerEjecucion()
            self.working_area.ResetConfigs()
            self.function_set.ResetConfigs()
            Application.putOnDeleteList(self.message)
            self.message = None

            image.LoadFromFile(self.DIRECTORIO+"gameplay/play_1.png")
            self.botonPlayStop.SetImage(image)
        else:
            self.working_area.Ejecutar(self.function_set)            
            image.LoadFromFile(self.DIRECTORIO+"gameplay/stop_1.png")
            self.botonPlayStop.SetImage(image)

        self.playing = not self.playing

    def BotonNextStep(self):
        self.playingStepByStep = True
        self.working_area.RunNextStep(self.function_set)

    def DefinirBotones(self):
        self.botonHome1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_1.png", 1200-157, 0, 157, 80)
        self.botonHome2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_2.png", 1200-157, 0, 157, 80)

        self.botonBack1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_back_1.png", 0, 0, 80, 80)
        
        self.botonBack2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_back_2.png", 0, 0, 80, 80)

        self.botonPlayStop = Application.createSfSprite(self.DIRECTORIO+"gameplay/play_1.png", 10, 91, 100, 70)

        self.botonStep = Application.createSfSprite(self.DIRECTORIO+"gameplay/stepbystep.png", 125, 100, 70, 50)

    def BotonHovered(self, x, y):
        if self.message != None:
            return "FADE"
        if(x>1200-157 and x<1200 and y>0 and y<60):
            return "HOME"
        if(x<80 and y<80):
            return "BACK"
        if (x>10 and x<110 and y>91 and y<143):
            return "PLAY_STOP"
        if (x>125 and x<195 and y>100 and y<150):
            return "STEP"
        
    def Pintar(self, boton):
        self.window.Draw(self.Fondo)
        if boton == "BACK":
            self.window.Draw(self.botonBack2)
        else:
            self.window.Draw(self.botonBack1)
        if boton == "HOME":
            self.window.Draw(self.botonHome2)
        else:
            self.window.Draw(self.botonHome1)
        self.window.Draw(self.botonPlayStop)
        self.window.Draw(self.botonStep)
        self.window.Draw(self.tittle)
        
        
        

    def DuplicateInstruction(self, ins):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/img_"+ins+".png")
        temp = sf.Sprite(image)
        temp.Resize(40, 40)
        temp.SetCenter(0, 0)
        temp.SetPosition(11, 569)
        return temp

    def GetImage(self, ins):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/img_"+ins+".png")
        return image

    def SetDraggingInstruction(self, ins):
        self.instruction_name = ins
        if self.temp == None:
            if ins != None:
                self.temp = self.DuplicateInstruction(ins)
        else:
            self.temp.SetImage(self.GetImage(ins))

        self.dragging_instruction = True
        

    def EndPuzzle(self):
        c = self.function_set.GetCount()
        #actualizar archivos
        #primero a ver si entra a los top 5!
        made_it = Application.updateTopFile("levels/" + self.backScreen + "/", str(self.puzzle_number) + "_top", Application.username, c)

        #ahora a ver si mejoro su marca personal.
        pers = Application.saveScore(Application.username, self.backScreen, self.puzzle_number, c)

        #levantar ventana final!
        from Game_Over import Game_Over
        nuevaVentana = Game_Over(c, made_it, pers)
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

        
    def Update(self):
        self.temp = None
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirBotones()
        q = False 
        while not q:
            x = input.GetMouseX()
            y = input.GetMouseY()
            boton = self.BotonHovered(x, y)
            frameTime = self.window.GetFrameTime()           
                
            while self.window.GetEvent(self.Evento):
                if self.slider.Update(frameTime, self.Evento, x, y) == True:
                    self.working_area.SetVelocity(self.slider.GetVelocity())
                
                if self.Evento.Type == sf.Event.Closed:
                    q = True
                    if self.sonidos != None:
                        self.sonidos.StopMenuMusic()
                    self.window.Close()
                        
                if self.Evento.Type == sf.Event.MouseButtonPressed:                    
                    print (str(x)+","+str(y))
                    self.instruction_name = self.toolbox.InstructionToolboxClicked(x, y)
                    ins = self.instruction_name
                    if ins != None and (not self.playing):
                        if ins != "INS_CLEAR":
                            if self.temp == None:
                                self.temp = self.DuplicateInstruction(ins)
                            else:
                                self.temp.SetImage(self.GetImage(ins))

                            self.dragging_instruction = True
                        else:
                            self.function_set.Clear()
                            self.toolbox.DisableClear()
                    else:
                        if not self.playing:
                            t = self.function_set.InstructionClicked(x, y, self)
                            if self.function_set.GetCount() == 0:
                                self.toolbox.DisableClear()
                        else:
                            t = False
                        if not t:
                            if boton == "BACK":
                                self.BotonBack()
                            elif boton == "HOME":
                                self.BotonHome()
                            elif boton == "PLAY_STOP":
                                self.BotonPlayStop()
                            elif boton == "STEP":
                                self.BotonNextStep()
                            elif boton == "TEST":
                                self.window.GetView().Zoom(1.01)
                            elif boton == "FADE":
                                Application.putOnDeleteList(self.message)
                                self.message = None
                if self.Evento.Type == sf.Event.MouseButtonReleased:
                    if self.dragging_instruction:
                        res = self.function_set.PlaceInstruction(x, y)
                        if res[0]:
                            if self.function_set.InsertInstruction(res[1], res[2], self.temp, self.instruction_name):
                                self.toolbox.EnableClear()
                                self.temp = None
                            
                        self.dragging_instruction = False
            if self.playing or self.playingStepByStep:
                resuelto = self.working_area.Update(frameTime)
                if resuelto == True:
                    self.EndPuzzle()
            self.window.Clear(sf.Color(255,255,255))
            self.Pintar(boton)
            self.goal.Pintar(self.window)
            self.working_area.Pintar(self.window)
            self.window.Draw(self.delimiter)
            
            self.toolbox.Pintar(self.window)
            self.slider.Pintar(self.window)
            self.function_set.Pintar(self.window)
            if self.dragging_instruction:
                self.temp.SetPosition(x - 22, y - 22)
                self.window.Draw(self.temp)
            if self.message != None:
                self.message.Pintar(self.window)
            self.window.Display()
