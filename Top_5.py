import sys
from PySFML import sf

class Top_5:
    DIRECTORIO =  "images/"
    def __init__(self, level, puzzle_number):
        self.width = 1200
        self.heigth = 700
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - TOP 5: "+ level + " PUZZLE " + str(puzzle_number), sf.Style.Close)
        self.Evento = sf.Event()
        self.sonidos = None

    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/TBG.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200, 700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)

    def DefinirBotones(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_home_1.png")
        self.botonHome1 = sf.Sprite(image)
        self.botonHome1.Resize(65, 60)
        self.botonHome1.SetCenter(0, 0)
        self.botonHome1.SetPosition(1135, 0)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_home_2.png")
        self.botonHome2 = sf.Sprite(image)
        self.botonHome2.Resize(65, 60)
        self.botonHome2.SetCenter(0, 0)
        self.botonHome2.SetPosition(1135, 0)
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_back_1.png")
        self.botonBack1 = sf.Sprite(image)
        self.botonBack1.Resize(80, 80)
        self.botonBack1.SetCenter(0, 0)
        self.botonBack1.SetPosition(0, 0)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_back_2.png")
        self.botonBack2 = sf.Sprite(image)
        self.botonBack2.Resize(80, 80)
        self.botonBack2.SetCenter(0, 0)
        self.botonBack2.SetPosition(0, 0)

    def BotonHovered(self, x, y):
        if(x>1135 and x<1200 and y>0 and y<60):
            return "HOME"
        if(x<80 and y<80):
            return "BACK"

    def Pintar(self, window, boton):
        window.Draw(self.Fondo)
        if boton == "HOME":
            window.Draw(self.botonHome2)
        else:
            window.Draw(self.botonHome1)
        if boton == "BACK":
            window.Draw(self.botonBack2)
        else:
            window.Draw(self.botonBack1)

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
                    if boton == "BACK":
                        self.Close()
                    if boton == "HOME":
                        self.BotonHome()

                if self.Evento.Type == sf.Event.MouseButtonReleased:
                    pass

            self.Pintar(self.window, boton)
            self.window.Display()

v = Top_5("GODMODE",5)
v.Update()
