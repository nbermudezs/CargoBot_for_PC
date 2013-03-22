import sys
from PySFML import sf

class Credits:
    DIRECTORIO =  "images/"
    def __init__(self):
        self.width = 1200
        self.heigth = 700
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "DRAG BOX - CREDITS!", sf.Style.Close)
        self.Evento = sf.Event()
        self.sonidos = None

    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/credits.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200, 700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)

    def DefinirBotones(self):
        pass

    def BotonHovered(self, x, y):
        if True:
            return "HOME"
        if False:
            return "EXIT"

    def Pintar(self, window, boton):
        window.Draw(self.Fondo)
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

            self.Pintar(self.window, boton)
            self.window.Display()

v = Credits()
v.Update()
