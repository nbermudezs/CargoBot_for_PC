import sys
import string
from PySFML import sf
from Sounds import Sounds

class Main_Screen:    
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
        self.sonidos = Sounds()
        self.sonidos.PlayMenuMusic()


    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/CargoBotBG2.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200, 700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/text_main2.png")
        self.text = sf.Sprite(image)
        self.text.Resize(1200, 700)
        self.text.SetCenter(0, 0)
        self.text.SetPosition(0,0)


    def DefinirBoton(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/START3.png")
        self.boton2 = sf.Sprite(image)
        self.boton2.Resize(1013-829,661-500)
        self.boton2.SetCenter(0, 0)
        self.boton2.SetPosition(832,500)
        

    def BotonCreditos(self):
       c = Creditos()
       c.Update()
       self.Update()
                
    def Pintar(self, x, y):
        self.window.Draw(self.Fondo)
        self.window.Draw(self.text)
        if(self.BotonHovered(x,y)=="START"):
            self.window.Draw(self.boton2)


    def BotonHovered(self, x, y):
        if(x>830 and x<1013 and y>500 and y<661):
            return "START"
        else:
            return "OTRO"

    def GoToPlayScreen(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()
    
    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirBoton()
        q = False 
        while not q:
            x = input.GetMouseX()
            y = input.GetMouseY()     
            while self.window.GetEvent(self.Evento):
                print self.Evento.Type
                if self.Evento.Type == sf.Event.Closed:
                    self.sonidos.StopMenuMusic()
                    self.window.Close()
                        
                if self.Evento.Type == sf.Event.MouseButtonPressed:
                    if(self.BotonHovered(x,y)=="START"):
                        self.GoToPlayScreen()
                    
                        
            self.window.Clear(self.blanco)
            self.Pintar(x, y)
            self.window.Display()       

if __name__ == "__main__":
    ven = Main_Screen()
    ven.Update() 
