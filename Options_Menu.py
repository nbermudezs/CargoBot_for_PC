import sys
import string
from PySFML import sf
from xml.etree.ElementTree import ElementTree as ET
from Application import Application
from xml.etree.ElementTree import Element

class Options_Menu:
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
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - OPTIONS", sf.Style.Close)
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)
        self.sonidos = None

        treeP = ET()
        treeP.parse("settings/settings.xml")
        root = treeP.getroot()
        self.lastplayer = root.find("lastplayer").text


    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/options_screen2.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200,700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)

    def DefinirBotones(self):
        #boton Play
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_play_1.png")
        self.btnPlay1 = sf.Sprite(image)
        self.btnPlay1.Resize(502-231, 457-297)
        self.btnPlay1.SetCenter(0, 0)
        self.btnPlay1.SetPosition(231, 297)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_play_2.png")
        self.btnPlay2 = sf.Sprite(image)
        self.btnPlay2.Resize(502-231, 457-297)
        self.btnPlay2.SetCenter(0, 0)
        self.btnPlay2.SetPosition(231, 297)

        #boton Cambiar player
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_change_2.png")
        self.btnChange2 = sf.Sprite(image)
        self.btnChange2.Resize(502-231, 655-496)
        self.btnChange2.SetCenter(0, 0)
        self.btnChange2.SetPosition(231, 496)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_change_1.png")
        self.btnChange1 = sf.Sprite(image)
        self.btnChange1.Resize(502-231, 655-496)
        self.btnChange1.SetCenter(0, 0)
        self.btnChange1.SetPosition(231, 496)

        #boton Crear player
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_new_1.png")
        self.btnCreate1 = sf.Sprite(image)
        self.btnCreate1.Resize(963-689, 457-297)
        self.btnCreate1.SetCenter(0, 0)
        self.btnCreate1.SetPosition(689, 297)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_new_2.png")
        self.btnCreate2 = sf.Sprite(image)
        self.btnCreate2.Resize(963-689, 457-297)
        self.btnCreate2.SetCenter(0, 0)
        self.btnCreate2.SetPosition(689, 297)

        #boton Exit
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_exit_1.png")
        self.btnExit1 = sf.Sprite(image)
        self.btnExit1.Resize(963-689, 457-297)
        self.btnExit1.SetCenter(0, 0)
        self.btnExit1.SetPosition(689, 496)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_exit_2.png")
        self.btnExit2 = sf.Sprite(image)
        self.btnExit2.Resize(963-689, 457-297)
        self.btnExit2.SetCenter(0, 0)
        self.btnExit2.SetPosition(689, 496)


    def DefinirWelcomeMsg(self):
        if self.lastplayer == None:
            text = "You haven't selected or created a username"
        else:
            text = "[ Welcome, "+self.lastplayer + "]"
        font = sf.Font()
        font = sf.Font.GetDefaultFont()
        #font.LoadFromFile('my_downloaded_font.ttf', 50)
        self.welcomemsg = sf.String(text, font)
        Application.username = self.lastplayer
        color = sf.Color(255, 255, 255)
        rect = self.welcomemsg.GetRect()
        self.welcomemsg.SetColor(color)
        self.welcomemsg.SetCenter(0,0)
        
        self.welcomemsg.SetSize(35)
        self.welcomemsg.SetPosition(1100 - rect.GetWidth(), 60)      


    def BotonPlay(self):
        if self.lastplayer == None:
            return
        from Level_Selection import Level_Selection
        nuevaVentana = Level_Selection()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonCambiar(self):
        from Change_Profile import Change_Profile
        nuevaVentana = Change_Profile()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()
        
    def BotonSalir(self):
        self.window.Close()

    def BotonCrear(self):
        from Create_Profile import Create_Profile
        nuevaVentana = Create_Profile()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()
                
    def Pintar(self, boton_hovered):
        self.window.Clear()
        self.window.Draw(self.Fondo)
        self.window.Draw(self.welcomemsg)        
        if(boton_hovered == "PLAY" and self.lastplayer != None):
            self.window.Draw(self.btnPlay2)
        else:
            self.window.Draw(self.btnPlay1)
            
        if(boton_hovered == "CREATE"):
            self.window.Draw(self.btnCreate2)
        else:
            self.window.Draw(self.btnCreate1)
            
        if(boton_hovered == "CHANGE"):
            self.window.Draw(self.btnChange2)
        else:
            self.window.Draw(self.btnChange1)
            
        if(boton_hovered == "EXIT"):
            self.window.Draw(self.btnExit2)
        else:
            self.window.Draw(self.btnExit1)

    def BotonHovered(self, x, y):
        if(x>231 and x<502 and y>297 and y<457):
            return "PLAY"
        if(x>231 and x<502 and y>496 and y<655):
            return "CHANGE"
        if(x>689 and x<963 and y>297 and y<457):
            return "CREATE"
        if(x>689 and x<963 and y>496 and y<655):
            return "EXIT"

    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirWelcomeMsg()
        self.DefinirBotones()
        quit = False 
        while not quit:
            x = input.GetMouseX()
            y = input.GetMouseY()     
            while self.window.GetEvent(self.Evento):
                if self.Evento.Type == sf.Event.Closed:
                    quit = True
                    self.sonidos.StopMenuMusic()
                        
                if self.Evento.Type == sf.Event.MouseButtonPressed:
                    boton = self.BotonHovered(x, y)
                    if(boton == "PLAY"):
                        self.BotonPlay()
                    elif(boton == "CREATE"):
                        self.BotonCrear()
                    elif(boton == "CHANGE"):
                        self.BotonCambiar()
                    elif(boton == "EXIT"):
                        self.BotonSalir()
                        
            self.Pintar(self.BotonHovered(x, y))
            self.window.Display()
        self.window.Close()


