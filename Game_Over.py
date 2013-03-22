import sys
from PySFML import sf
from Application import Application

class Game_Over:
    DIRECTORIO =  "images/"
    def __init__(self, score, made_it, personal_mark):
        self.width = 1200
        self.heigth = 700
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "DRAG BOX - CONGRATULATIONS!", sf.Style.Close)
        self.Evento = sf.Event()
        self.sonidos = None

        if not (personal_mark in ["BETTER", "NOT_BETTER", "FIRST_TIME", "EQUAL"] or made_it):
            self.img_score = Application.createSfSprite(self.DIRECTORIO+"scores/"+str(score)+".png", 181, 350, 1022-181, 336 - 251)
        else:
            self.img_score = Application.createSfSprite(self.DIRECTORIO+"scores/"+str(score)+".png", 181, 251, 1022-181, 336 - 251)
        
        if made_it:        
            self.img_gratz = Application.createSfSprite(self.DIRECTORIO+"scores/gratz.png", 181, 330, 1022 - 181, 250)
        elif personal_mark == "BETTER":
            self.img_gratz = Application.createSfSprite(self.DIRECTORIO+"scores/better.png", 181, 330, 1022 - 181, 250)
        elif personal_mark == "NOT_BETTER":
            self.img_gratz = Application.createSfSprite(self.DIRECTORIO+"scores/worse.png", 181, 330, 1022 - 181, 250)
        elif personal_mark == "FIRST_TIME":
            self.img_gratz = Application.createSfSprite(self.DIRECTORIO+"scores/first.png", 181, 330, 1022 - 181, 250)
        elif personal_mark == "EQUAL":
            self.img_gratz = Application.createSfSprite(self.DIRECTORIO+"scores/equal.png", 181, 330, 1022 - 181, 250)
        
    def DefinirFondo(self):
        self.Fondo0 = Application.createSfSprite(self.DIRECTORIO+"bgs/TBG3.png", 0, 0, 1200, 700)
        self.Fondo = Application.createSfSprite(self.DIRECTORIO+"bgs/GBG.png", 0, 0, 1200, 700)

        self.credits = Application.createSfSprite(self.DIRECTORIO+"scores/credits.png", 0, 700 - 43, 113, 43)
        self.mmenu = Application.createSfSprite(self.DIRECTORIO+"scores/main_menu.png", 1200 - 197, 700 - 43, 197, 43)

        self.credits_2 = Application.createSfSprite(self.DIRECTORIO+"scores/credits_2.png", 0, 700 - 43, 113, 43)
        self.mmenu_2 = Application.createSfSprite(self.DIRECTORIO+"scores/main_menu_2.png", 1200 - 197, 700 - 43, 197, 43)

    def DefinirBotones(self):
        pass

    def BotonHovered(self, x, y):
        if x>1003 and y>657:
            return "MMENU"
        if x<113 and y>657:
            return "CREDITS"

    def Pintar(self, boton):
        self.window.Draw(self.Fondo0)
        self.window.Draw(self.Fondo)
        self.window.Draw(self.img_score)
        if self.img_gratz != None:
            self.window.Draw(self.img_gratz)
        if boton == "CREDITS":
            self.window.Draw(self.credits_2)
        else:
            self.window.Draw(self.credits)
        if boton == "MMENU":
            self.window.Draw(self.mmenu_2)
        else:
            self.window.Draw(self.mmenu)

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
                    print (str(x) + "," + str(y))
                    if boton == "MMENU":
                        self.BotonHome()
                    if boton == "CREDITS":
                        pass

                if self.Evento.Type == sf.Event.MouseButtonReleased:
                    pass
            
            self.window.Clear(sf.Color(255,255,255))
            self.Pintar(boton)
            self.window.Display()

#v = Game_Over(3, False, "NOT_BETTER")
#v.Update()
