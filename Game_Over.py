import sys
from PySFML import sf
from Application import Application

class Game_Over:
    DIRECTORIO =  "images/"
    def __init__(self, score):
        self.width = 1200
        self.heigth = 700
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - CONGRATULATIONS!", sf.Style.Close)
        self.Evento = sf.Event()
        self.sonidos = None
        
        self.img_score = Application.createSfSprite(self.DIRECTORIO+"scores/"+str(score)+".png", 0, 0, 1200, 700)

    def DefinirFondo(self):
        self.img_score = Application.createSfSprite(self.DIRECTORIO+"bgs/TBG.png", 0, 0, 1200, 700)

    def DefinirBotones(self):
        pass

    def BotonHovered(self, x, y):
        return ""
        if True:
            return "HOME"
        if False:
            return "EXIT"

    def Pintar(self, boton):
        self.window.Draw(self.Fondo)
        self.window.Draw(self.img_score)
        if boton == "HOME":
            pass
        if boton == "EXIT":
            pass

    def Close(self):
        if self.sonidos != None:
            self.sonidos.StopMenuMusic()
        self.window.Close()

    def BotonHome(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def Update(self):
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
                if self.Evento.Type == sf.Event.Closed:
                    q = True
                    self.Close()

                if self.Evento.Type == sf.Event.MouseButtonPressed:
                    if boton == "EXIT":
                        self.Close()
                    if boton == "HOME":
                        self.BotonHome()

                if self.Evento.Type == sf.Event.MouseButtonReleased:
                    pass
            
            self.window.Clear(sf.Color(255,255,255))
            self.Pintar(boton)
            self.window.Display()

