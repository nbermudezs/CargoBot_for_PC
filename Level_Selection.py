import sys
import string
from PySFML import sf

class Level_Selection:
    width = 0
    heigth = 0
    Evento = None
    window = None
    negro = None
    blanco = None
    BombermanB = None
    negro = None
    #para pintar
    Mapa =None
    Fondo = None
    DIRECTORIO = "images/"
    current_mapa = ""
	
    def __init__(self):
        self.width = 1200
        self.heigth = 700
        self.blanco = sf.Color(250, 250, 250)
        self.negro =  sf.Color(0, 0, 0)
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - LEVEL SELECTION", sf.Style.Close)
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)
        self.username = ""
        self.sonidos = None


    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/level_selection_screen2.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200,700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)

    def DefinirBotones(self):
        #boton home
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_home_1.png")
        self.botonHome1 = sf.Sprite(image)
        self.botonHome1.Resize(85, 80)
        self.botonHome1.SetCenter(0, 0)
        self.botonHome1.SetPosition(1115, 0)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_home_2.png")
        self.botonHome2 = sf.Sprite(image)
        self.botonHome2.Resize(85, 80)
        self.botonHome2.SetCenter(0, 0)
        self.botonHome2.SetPosition(1115, 0)

        #boton tutorial
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_tutorial_1.png")
        self.botonTutorial1 = sf.Sprite(image)
        self.botonTutorial1.Resize(380-57, 605-287)
        self.botonTutorial1.SetCenter(0, 0)
        self.botonTutorial1.SetPosition(57, 292)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_tutorial_2.png")
        self.botonTutorial2 = sf.Sprite(image)
        self.botonTutorial2.Resize(380-57, 605-287)
        self.botonTutorial2.SetCenter(0, 0)
        self.botonTutorial2.SetPosition(57, 292)

        #boton easy
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_easy_1.png")
        self.botonEasy1 = sf.Sprite(image)
        self.botonEasy1.Resize(380-57, 605-287)
        self.botonEasy1.SetCenter(0, 0)
        self.botonEasy1.SetPosition(440, 292)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_easy_2.png")
        self.botonEasy2 = sf.Sprite(image)
        self.botonEasy2.Resize(380-57, 605-287)
        self.botonEasy2.SetCenter(0, 0)
        self.botonEasy2.SetPosition(440, 292)

        #boton god_mode
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_god_1.png")
        self.botonGod1 = sf.Sprite(image)
        self.botonGod1.Resize(380-57, 605-287)
        self.botonGod1.SetCenter(0, 0)
        self.botonGod1.SetPosition(820, 292)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_god_2.png")
        self.botonGod2 = sf.Sprite(image)
        self.botonGod2.Resize(380-57, 605-287)
        self.botonGod2.SetCenter(0, 0)
        self.botonGod2.SetPosition(820, 292)

    def BotonHome(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonTutorial(self):
        from Tutorial_Puzzles import Tutorial_Puzzles
        nuevaVentana = Tutorial_Puzzles()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonEasy(self):
        from Easy_Puzzles import Easy_Puzzles
        nuevaVentana = Easy_Puzzles()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonMisc(self):
        from Misc_Puzzles import Misc_Puzzles
        nuevaVentana = Misc_Puzzles()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonHovered(self, x, y):
        if(x>1115 and x<1200 and y>0 and y<80):
            return "HOME"
        if(x>57 and x<380 and y>292 and y<605):
            return "TUTORIAL"
        if(x>440 and x<763 and y>292 and y<605):
            return "EASY"
        if(x>820 and x<1143 and y>292 and y<605):
            return "GODMODE"
                
    def Pintar(self, boton):
        self.window.Draw(self.Fondo)      
        
        
        if(boton == "HOME"):
            self.window.Draw(self.botonHome2)
        else:
            self.window.Draw(self.botonHome1)
        if(boton == "EASY"):
            self.window.Draw(self.botonEasy2)
        else:
            self.window.Draw(self.botonEasy1)
        if(boton == "TUTORIAL"):
            self.window.Draw(self.botonTutorial2)
        else:
            self.window.Draw(self.botonTutorial1)
        if(boton == "GODMODE"):
            self.window.Draw(self.botonGod2)
        else:
            self.window.Draw(self.botonGod1)

    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirBotones()
        quit = False
        while not quit:
            x = input.GetMouseX()
            y = input.GetMouseY()
            boton = self.BotonHovered(x, y)
            while self.window.GetEvent(self.Evento):
                if self.Evento.Type == sf.Event.Closed:
                    quit = True
                    self.sonidos.StopMenuMusic()
                    
                if self.Evento.Type == sf.Event.MouseButtonPressed:
                    if(boton == "HOME"):
                        self.BotonHome()
                    if(boton == "TUTORIAL"):
                        self.BotonTutorial()
                    if(boton == "EASY"):
                        self.BotonEasy()
                    if(boton == "GODMODE"):
                        self.BotonMisc()
                    
            self.window.Clear(self.blanco)
            self.Pintar(boton)
            self.window.Display()
        self.window.Close()
