import sys
from PySFML import sf
from Application import Application

class Top_5:
    DIRECTORIO =  "images/"
    def __init__(self, level, puzzle_number):
        self.backScreen = level
        self.width = 1200
        self.heigth = 700
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - TOP 5: "+ level + " PUZZLE " + str(puzzle_number), sf.Style.Close)
        self.Evento = sf.Event()
        self.sonidos = None

        self.data = Application.getTopScores(level, puzzle_number)

        self.posiciones = [(909, 190), (702, 289), (494, 386), (290, 485), (79, 582)]
        self.star_posiciones = [(1088, 222),(877, 319),(671, 412),(465, 509),(257, 609)]
        self.userSize = (289 - 79, 638 - 574)
        self.starSize = (324 - 257, 674 - 609)

        self.FillInTops(self.data, self.posiciones, self.userSize)
            
    def FillInTops(self, data, posiciones, size):
        self.tops = []
        self.stars = []
        for i in range(len(data)):
            if data[i][0] == "__EMPTY__":
                t = sf.String("----------")                
            else:
                t = sf.String(data[i][0])
                print "valor: " + str(data[i][1])
                self.stars.append(Application.createSfSprite("images/buttons/stars/" + str(data[i][1]) + ".png",
                                                             self.star_posiciones[i][0], self.star_posiciones[i][1],
                                                             self.starSize[0], self.starSize[1]))
                                  
            color = sf.Color(0, 0, 0)
            rect = t.GetRect()
            t.SetColor(color)
            t.SetCenter(0,0)        
            t.SetSize(25)
            t.SetPosition(posiciones[i][0] + (size[0] - rect.GetWidth())/2 + 5, posiciones[i][1] + (size[1] - rect.GetHeight())/2)
            self.tops.append(t)
    
    def DefinirFondo(self):
        self.Fondo = Application.createSfSprite(self.DIRECTORIO + "bgs/Top_BG.png", 0, 0, 1200, 700)
        self.Fondo0 = Application.createSfSprite(self.DIRECTORIO + "bgs/TBG3.png", 0, 0, 1200, 700)

    def DefinirBotones(self):
        self.botonHome1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_1.png", 1200-157, 0, 157, 80)
        self.botonHome2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_2.png", 1200-157, 0, 157, 80)
        
        self.botonBack1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_back_1.png", 0, 0, 80, 80)
        self.botonBack2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_back_2.png", 0, 0, 80, 80)

    def BotonHovered(self, x, y):
        if(x>1200-157 and x<1200 and y>0 and y<80):
            return "HOME"
        if(x<80 and y<80):
            return "BACK"

    def Pintar(self, window, boton):
        window.Draw(self.Fondo0)
        window.Draw(self.Fondo)
        if boton == "HOME":
            window.Draw(self.botonHome2)
        else:
            window.Draw(self.botonHome1)
        if boton == "BACK":
            window.Draw(self.botonBack2)
        else:
            window.Draw(self.botonBack1)

        for top in self.tops:
            window.Draw(top)
        for star in self.stars:
            window.Draw(star)

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

    def BotonBack(self):
        if not (self.backScreen in ["TUTORIAL", "EASY", "GODMODE"]):
            return
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
                    print ("POSITION TOP_5: " + str(x) + "," + str(y))
                    if boton == "BACK":
                        self.BotonBack()
                    if boton == "HOME":
                        self.BotonHome()

                if self.Evento.Type == sf.Event.MouseButtonReleased:
                    pass

            self.Pintar(self.window, boton)
            self.window.Display()
