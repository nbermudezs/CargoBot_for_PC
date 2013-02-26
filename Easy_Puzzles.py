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
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - PUZZLES (EASY)", sf.Style.Close)
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)

        self.scores = Application.getScores(Application.username, "EASY")


    def DefinirFondo(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"bgs/easy.png")
        self.Fondo = sf.Sprite(image)
        self.Fondo.Resize(1200, 700)
        self.Fondo.SetCenter(0, 0)
        self.Fondo.SetPosition(0,0)
        

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

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_back_1.png")
        self.botonBack1 = sf.Sprite(image)
        self.botonBack1.Resize(100, 100)
        self.botonBack1.SetCenter(0, 0)
        self.botonBack1.SetPosition(0, 0)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_back_2.png")
        self.botonBack2 = sf.Sprite(image)
        self.botonBack2.Resize(100, 100)
        self.botonBack2.SetCenter(0, 0)
        self.botonBack2.SetPosition(0, 0)


        #botones numero hover
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_1_2.png")
        self.num1_2 = sf.Sprite(image)
        self.num1_2.Resize(360-77, 338-199)
        self.num1_2.SetCenter(0, 0)
        self.num1_2.SetPosition(77, 199)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_2_2.png")
        self.num2_2 = sf.Sprite(image)
        self.num2_2.Resize(360-77, 338-199)
        self.num2_2.SetCenter(0, 0)
        self.num2_2.SetPosition(451, 199)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_3_2.png")
        self.num3_2 = sf.Sprite(image)
        self.num3_2.Resize(360-77, 338-199)
        self.num3_2.SetCenter(0, 0)
        self.num3_2.SetPosition(822, 199)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_4_2.png")
        self.num4_2 = sf.Sprite(image)
        self.num4_2.Resize(360-77, 338-199)
        self.num4_2.SetCenter(0, 0)
        self.num4_2.SetPosition(77, 446)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_5_2.png")
        self.num5_2 = sf.Sprite(image)
        self.num5_2.Resize(360-77, 338-199)
        self.num5_2.SetCenter(0, 0)
        self.num5_2.SetPosition(451, 446)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_6_2.png")
        self.num6_2 = sf.Sprite(image)
        self.num6_2.Resize(360-77, 338-199)
        self.num6_2.SetCenter(0, 0)
        self.num6_2.SetPosition(822, 446)
        #botones numero
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_1.png")
        self.num1 = sf.Sprite(image)
        self.num1.Resize(360-77, 338-199)
        self.num1.SetCenter(0, 0)
        self.num1.SetPosition(77, 199)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_2.png")
        self.num2 = sf.Sprite(image)
        self.num2.Resize(360-77, 338-199)
        self.num2.SetCenter(0, 0)
        self.num2.SetPosition(451, 199)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_3.png")
        self.num3 = sf.Sprite(image)
        self.num3.Resize(360-77, 338-199)
        self.num3.SetCenter(0, 0)
        self.num3.SetPosition(822, 199)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_4.png")
        self.num4 = sf.Sprite(image)
        self.num4.Resize(360-77, 338-199)
        self.num4.SetCenter(0, 0)
        self.num4.SetPosition(77, 446)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_5.png")
        self.num5 = sf.Sprite(image)
        self.num5.Resize(360-77, 338-199)
        self.num5.SetCenter(0, 0)
        self.num5.SetPosition(451, 446)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/button_6.png")
        self.num6 = sf.Sprite(image)
        self.num6.Resize(360-77, 338-199)
        self.num6.SetCenter(0, 0)
        self.num6.SetPosition(822, 446)
        

    def DefinirEstrellas(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/stars/1.png")
        star1 = sf.Sprite(image)
        star1.Resize(64, 64)
        star1.SetCenter(0, 0)
        star1.SetPosition(46, 294)
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/stars/2.png")
        star2 = sf.Sprite(image)
        star2.Resize(64, 64)
        star2.SetCenter(0, 0)
        star2.SetPosition(421, 294)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/stars/3.png")
        star3 = sf.Sprite(image)
        star3.Resize(64, 64)
        star3.SetCenter(0, 0)
        star3.SetPosition(795, 551)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/stars/4.png")
        star4 = sf.Sprite(image)
        star4.Resize(64, 64)
        star4.SetCenter(0, 0)
        star4.SetPosition(46, 551)
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/stars/5.png")
        star5 = sf.Sprite(image)
        star5.Resize(64, 64)
        star5.SetCenter(0, 0)
        star5.SetPosition(421, 551)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/stars/6.png")
        star6 = sf.Sprite(image)
        star6.Resize(64, 64)
        star6.SetCenter(0, 0)
        star6.SetPosition(795, 551)

        self.stars = []
        self.stars.append(star1)
        self.stars.append(star2)
        self.stars.append(star3)
        self.stars.append(star4)
        self.stars.append(star5)
        self.stars.append(star6)

    def DefinirTops(self):
        self.tops = []
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/top.png")
        top = sf.Sprite(image)
        top.Resize(110, 64)
        top.SetCenter(0, 0)
        top.SetPosition(292, 190)        
        self.tops.append(top)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/top.png")
        top = sf.Sprite(image)
        top.Resize(110, 64)
        top.SetCenter(0, 0)
        top.SetPosition(666, 190)        
        self.tops.append(top)
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/top.png")
        top = sf.Sprite(image)
        top.Resize(110, 64)
        top.SetCenter(0, 0)
        top.SetPosition(1037, 190)        
        self.tops.append(top)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/top.png")
        top = sf.Sprite(image)
        top.Resize(110, 64)
        top.SetCenter(0, 0)
        top.SetPosition(292, 438)        
        self.tops.append(top)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/top.png")
        top = sf.Sprite(image)
        top.Resize(110, 64)
        top.SetCenter(0, 0)
        top.SetPosition(666, 438)        
        self.tops.append(top)
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/top.png")
        top = sf.Sprite(image)
        top.Resize(110, 64)
        top.SetCenter(0, 0)
        top.SetPosition(1037, 438)        
        self.tops.append(top)

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
        if(x>1115 and x<1200 and y>0 and y<80):
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
                    if boton == "BACK":
                        self.BotonBack()
                    if boton in ["1","2","3","4","5","6"]:
                        self.LetsPlay(boton)
                        
            self.window.Clear()
            self.Pintar(boton)
            self.window.Display()
        self.window.Close()
