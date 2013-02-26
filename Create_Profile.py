import sys
import string
from PySFML import sf
from Application import Application

class Create_Profile:    
    def __init__(self):
        self.width = 1200
        self.heigth = 700
        self.blanco = sf.Color(250, 250, 250)
        self.negro =  sf.Color(0, 0, 0)
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - CREATE PROFILE", sf.Style.Close)
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)
        self.DIRECTORIO = "images/"


    def DefinirFondo(self):
        self.Fondo = Application.createSfSprite(self.DIRECTORIO+"bgs/CB2.png", 0, 0, 1200, 700)
        self.text = Application.createSfSprite(self.DIRECTORIO+"bgs/text_create.png", 0, 0, 1200, 700)

    def BotonCreate(self):
        if self.name_text != "":
            Application.createProfile(self.name_text)
            self.BotonHome()

    def BotonHome(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()


    def DefinirBotones(self):
        #boton create
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_create_1.png")
        self.boton1 = sf.Sprite(image)
        self.boton1.Resize(367,140)
        self.boton1.SetCenter(0, 0)
        self.boton1.SetPosition(434,504)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_create_2.png")
        self.boton2 = sf.Sprite(image)
        self.boton2.Resize(367,140)
        self.boton2.SetCenter(0, 0)
        self.boton2.SetPosition(434,504)

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

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/CREATE.png")
        self.create = sf.Sprite(image)
        self.create.Resize(1013-829,661-500)
        self.create.SetCenter(0, 0)
        self.create.SetPosition(688,348)

    def DefinirTextBox(self):
        font = sf.Font()
        font = sf.Font.GetDefaultFont()
        #font.load_from_file('dk.ttf')
        #font = sf.Font.load_from_file('dk.ttf')
        self.name_text = ""
        self.name = sf.String(self.name_text, font)
        color = sf.Color(255, 207, 159)
        self.name.SetColor(color)
        self.name.SetCenter(0,0)
        
        self.name.SetSize(45)
        self.name.SetPosition(237, 200)

    def PintarTexto(self):
        width = self.name.GetRect().GetWidth()
        x = 237 + (727 - width)/2
        self.name.SetText(self.name_text)
        self.name.SetPosition(x, 200)
        self.window.Draw(self.name)
                
    def Pintar(self, boton):
        self.window.Draw(self.Fondo)
        self.window.Draw(self.text)
        self.PintarTexto()
        self.window.Draw(self.botonHome1)
        if(boton == "CREATE"):
            self.window.Draw(self.create)
        if(boton == "HOME"):
            self.window.Draw(self.botonHome2)


    def BotonHovered(self, x, y):
        if(x>688 and x<872 and y>348 and y<509):
            return "CREATE"
        if(x>1115 and x<1200 and y>0 and y<80):
            return "HOME"

    def AppendToText(self, text):
        if text != 8 and self.name.GetRect().GetWidth()<600:
            self.name_text += unichr(text)
        if text == 277 and self.name.GetRect().GetWidth()<600:
            self.name_text += " "
        if text == 279 and len(self.name_text)>0:
            self.name_text = self.name_text[:len(self.name_text)-2]
            
    
    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirBotones()
        self.DefinirTextBox()
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
                    if(boton == "CREATE"):
                        self.BotonCreate()
                    if(boton == "HOME"):
                        self.BotonHome()

                if self.Evento.Type == sf.Event.KeyPressed:
                    self.AppendToText(self.Evento.Text.Unicode)
            
            self.Pintar(boton)
            self.window.Display()
        self.window.Close()
