import sys
import string
from PySFML import sf
from Application import Application

class Easy_Puzzles:    
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
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "DRAG BOX - PUZZLES (EASY)", sf.Style.Close)
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)

        self.scores = Application.getScores(Application.username, "EASY")


    def DefinirFondo(self):
        self.Fondo = Application.createSfSprite(self.DIRECTORIO+"bgs/easy.png", 0, 0, 1200, 700)

    def BotonHome(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonBack(self):
        from Level_Selection import Level_Selection
        nuevaVentana = Level_Selection()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def LetsPlay(self, boton):
        from Game_Window import Game_Window
        nuevaVentana = Game_Window("EASY", int(boton))
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def ShowTop(self, boton):
        from Top_5 import Top_5
        nuevaVentana = Top_5("EASY", boton)
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def DefinirBotones(self):
        self.botonHome1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_1.png", 1200-157, 0, 157, 80)
        self.botonHome2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_2.png", 1200-157, 0, 157, 80)
        
        self.botonBack1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_back_1.png", 0, 0, 80, 80)
        self.botonBack2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_back_2.png", 0, 0, 80, 80)


        #botones numero hover
        self.num1_2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_1_2.png", 77, 199, 360 - 77, 338 - 199)
        self.num2_2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_2_2.png", 451, 199, 360 - 77, 338 - 199)
        self.num3_2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_3_2.png", 822, 199, 360 - 77, 338 - 199)
        self.num4_2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_4_2.png", 77, 446, 360 - 77, 338 - 199)
        self.num5_2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_5_2.png", 451, 446, 360 - 77, 338 - 199)
        self.num6_2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_6_2.png", 822, 446, 360 - 77, 338 - 199)
        
        #botones numero
        self.num1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_1.png", 77, 199, 360 - 77, 338 - 199)
        self.num2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_2.png", 451, 199, 360 - 77, 338 - 199)
        self.num3 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_3.png", 822, 199, 360 - 77, 338 - 199)
        self.num4 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_4.png", 77, 446, 360 - 77, 338 - 199)
        self.num5 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_5.png", 451, 446, 360 - 77, 338 - 199)
        self.num6 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_6.png", 822, 446, 360 - 77, 338 - 199)
        

    def DefinirEstrellas(self):
        self.stars = []
        positions = [(46, 294), (421, 294), (795, 294), (46, 551), (421, 551), (795, 551)]
        for i in range(6):
            self.stars.append(Application.createSfSprite(self.DIRECTORIO+"buttons/stars/"+str(i+1)+".png", positions[i][0], positions[i][1], 64, 64))

    def DefinirTops(self):
        self.tops = []
        positions = [(292,190), (666,190), (1037,190), (292,438), (666,438), (1037,438)]

        for i in range(6):
            self.tops.append(Application.createSfSprite(self.DIRECTORIO+"buttons/top.png", positions[i][0], positions[i][1], 110, 64))

    def PintarTops(self):
        for top in self.tops:
            self.window.Draw(top)

    def PintarEstrellas(self):
        image = sf.Image()
        for i in self.scores:
            if i[1]>"0":
                image.LoadFromFile(self.DIRECTORIO+"buttons/stars/"+i[1]+".png")
                self.stars[int(i[0])-1].SetImage(image)
                self.window.Draw(self.stars[int(i[0])-1])

                    
    def Pintar(self, boton):
        self.window.Draw(self.Fondo)
        if boton == "1":
            self.window.Draw(self.num1_2)
        else:
            self.window.Draw(self.num1)
        if boton == "2":
            self.window.Draw(self.num2_2)
        else:
            self.window.Draw(self.num2)
        if boton == "3":
            self.window.Draw(self.num3_2)
        else:
            self.window.Draw(self.num3)
        if boton == "4":
            self.window.Draw(self.num4_2)
        else:
            self.window.Draw(self.num4)
        if boton == "5":
            self.window.Draw(self.num5_2)
        else:
            self.window.Draw(self.num5)
        if boton == "6":
            self.window.Draw(self.num6_2)
        else:
            self.window.Draw(self.num6)
        self.PintarEstrellas()
        self.PintarTops()
        
        if(boton == "HOME"):
            self.window.Draw(self.botonHome2)
        else:
            self.window.Draw(self.botonHome1)

        if boton == "BACK":
            self.window.Draw(self.botonBack2)
        else:
            self.window.Draw(self.botonBack1)


    def BotonHovered(self, x, y):
        for i in range(6):
            xi = self.tops[i].GetPosition()[0]
            yi = self.tops[i].GetPosition()[1]
            w = self.tops[i].GetSize()[0]
            h = self.tops[i].GetSize()[1]
            if(x<xi+w and x>xi and y<yi+h and y>yi):
                return ("TOP", i+1)
        if(x>1200-157 and x<1200 and y>0 and y<80):
            return "HOME"
        if(x<100 and y<100):
            return "BACK"
        if (x<360 and x>77 and y<338 and y>199):
            return "1"
        if(x<734 and x>451 and y<338 and y>199):
            return "2"
        if(x<1105 and x>882 and y<338 and y>199):
            return "3"
        if (x<360 and x>77 and y<585 and y>446):
            return "4"
        if(x<734 and x>451 and y<585 and y>446):
            return "5"
        if(x<1105 and x>882 and y<585 and y>446):
            return "6"
        return (None, None)
    
    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirBotones()
        self.DefinirTops()
        self.DefinirEstrellas()
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
                    if boton == "HOME":
                        self.BotonHome()
                    elif boton == "BACK":
                        self.BotonBack()
                    elif boton in ["1","2","3","4","5","6"]:
                        self.LetsPlay(boton)
                    elif boton[0] == "TOP":
                        self.ShowTop(boton[1])
                        
            self.window.Clear()
            self.Pintar(boton)
            self.window.Display()
        self.window.Close()
