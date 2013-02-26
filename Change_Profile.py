import sys
import math
import string
from PySFML import sf
from Application import Application
from xml.etree.ElementTree import ElementTree as ET
from xml.etree.ElementTree import Element

class Change_Profile:    
    Evento = None
    window = None
    Fondo = None
    DIRECTORIO = "images/"    
    
	
    def __init__(self):
        self.width = 1200
        self.heigth = 700
        self.blanco = sf.Color(250, 250, 250)
        self.negro =  sf.Color(0, 0, 0)
        self.window = sf.RenderWindow(sf.VideoMode(self.width, self.heigth), "CARGO BOT - CHANGE PROFILE", sf.Style.Close)
        self.Evento = sf.Event()
        self.window.SetFramerateLimit(60)
        self.usernames = Application.getFiles("profiles/")

        self.isSelected = False
        self.xSelected = 0
        self.ySelected = 0
        self.name_selected = None


    def DefinirFondo(self):
        self.Fondo = Application.createSfSprite(self.DIRECTORIO+"bgs/change_profile.png", 0, 0, 1200, 700)

    def BotonHome(self):
        self.cambiarVentana()

    def DefinirBotones(self):
        self.boton1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_choose_1.png", 434, 564, 367, 100)
        self.boton2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_choose_2.png", 434, 564, 367, 100)
        
        self.botonHome1 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_1.png", 1115, 0, 85, 80)
        self.botonHome2 = Application.createSfSprite(self.DIRECTORIO+"buttons/button_home_2.png", 1115, 0, 85, 80)
        
        self.botonPrev1 = Application.createSfSprite(self.DIRECTORIO+"buttons/scroll_prev_1.png", 0, 0, 130, 700)
        self.botonPrev2 = Application.createSfSprite(self.DIRECTORIO+"buttons/scroll_prev_2.png", 0, 0, 130, 700)

        self.botonNext1 = Application.createSfSprite(self.DIRECTORIO+"buttons/scroll_next_1.png", 1070, 0, 130, 700)
        self.botonNext2 = Application.createSfSprite(self.DIRECTORIO+"buttons/scroll_next_2.png", 1070, 0, 130, 700)


    def DefinirSeleccionado(self):
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"buttons/selected.png")
        self.selected = sf.Sprite(image)
        self.selected.Resize(200, 45)
        self.selected.SetCenter(0, 0)

    def DefinirUsuarios(self):
        self.usuarios = []
        self.usuarios.append([])
        self.usuarios.append([])
        self.usuarios.append([])
        for u in self.usuarios:
            u.append(sf.String(''))
            u.append(sf.String(''))
            u.append(sf.String(''))
        for i in range(3):
            for j in range(3):
                self.SetConfTexto(self.usuarios[i][j], 200 + i*(444-131),
                                  245 + j*(386-275))

        t = len(self.usernames)
        self.nextUser = 0
        if(t>9):
            self.nextUser = 9
            t = 9
        ii = int(math.ceil(t/3.0))
        jj = t%3
        if (jj == 0):
            jj = 3
        for i in range(ii-1):
            for j in range(3):
                self.usuarios[i][j].SetText(self.usernames[i*3+j])
        for j in range(jj):
            self.usuarios[ii-1][j].SetText(self.usernames[(ii-1)*3+j])

        print "next?: " + str(self.nextUser)
        

    def SetConfTexto(self, sfString, x, y):
        self.font = sf.Font()
        color = sf.Color(0, 0, 0)
        sfString.SetColor(color)
        sfString.SetCenter(0,0)
        
        sfString.SetSize(25)
        sfString.SetPosition(x, y)

    def LimpiarUsuarios(self):
        self.isSelected = False
        self.name_selected = None
        for i in range(3):
            for j in range(3):
                self.usuarios[i][j].SetText('')

    def UsuarioSeleccionado(self, x, y):
        collision = sf.IntRect(int(x), int(y), 200, 45)

        for i in range(3):
            for j in range(3):
                collision.Top = self.usuarios[i][j].GetPosition()[1]
                collision.Bottom = self.usuarios[i][j].GetPosition()[1] + 45
                collision.Left = self.usuarios[i][j].GetPosition()[0]
                collision.Right = self.usuarios[i][j].GetPosition()[0] + 200

                if(collision.Contains(int(x), int(y))):                   
                    
                    if(self.nextUser%9==0):
                        t = self.nextUser - 9
                    else:
                        t = self.nextUser - self.nextUser%9
                        
                    if len(self.usernames)<=t+i*3+j:
                        return
                    self.name_selected = self.usernames[t+i*3+j]
                    self.isSelected = True
                    self.xSelected = i
                    self.ySelected = j
                    self.selected.SetPosition(self.usuarios[i][j].GetPosition()[0] - 10,
                                              self.usuarios[i][j].GetPosition()[1] - 3)

    def SiguientesUsuarios(self):
        if self.nextUser>=len(self.usernames):
            return 
        self.LimpiarUsuarios()
        
        if(len(self.usernames)-self.nextUser>9):
            t = 9
        else:
            t = len(self.usernames)-self.nextUser
        ii = int(math.ceil(t/3.0))
        jj = t%3
        if (jj == 0):
            jj = 3
        for i in range(ii-1):
            for j in range(3):
                self.usuarios[i][j].SetText(self.usernames[self.nextUser + i*3+j])
        for j in range(jj):
            self.usuarios[ii-1][j].SetText(self.usernames[self.nextUser + (ii-1)*3+j])

        self.nextUser = self.nextUser + t

    def AnterioresUsuarios(self):
        self.LimpiarUsuarios()
        self.nextUser = self.nextUser - (self.nextUser%9) - 9
        if (self.nextUser < 0):
            self.nextUser = 0
            return
        self.LimpiarUsuarios()
        if(len(self.usernames)-self.nextUser>9):
            t = 9
        else:
            t = len(self.usernames)-self.nextUser
        ii = int(math.ceil(t/3.0))
        jj = t%3
        if (jj == 0):
            jj = 3
        for i in range(ii-1):
            for j in range(3):
                self.usuarios[i][j].SetText(self.usernames[self.nextUser + i*3+j])
        for j in range(jj):
            self.usuarios[ii-1][j].SetText(self.usernames[self.nextUser + (ii-1)*3+j])

        self.nextUser = self.nextUser + t

    def BotonHome(self):
        from Options_Menu import Options_Menu
        nuevaVentana = Options_Menu()
        nuevaVentana.sonidos = self.sonidos
        self.window.Close()
        nuevaVentana.Update()

    def BotonSelect(self):
        if (self.name_selected == None):
            return
        treeP = ET()
        treeP.parse("settings/settings.xml")
        root = treeP.getroot()
        lastplayer = root.find("lastplayer")
        lastplayer.text = self.name_selected
        treeP.write("settings/settings.xml")

    def PintarUsuarios(self):
        for i in range(3):
            for j in range(3):
                if(self.isSelected):
                    if(i==self.xSelected and j==self.ySelected):
                        self.window.Draw(self.selected)
                self.window.Draw(self.usuarios[i][j])
                
    
    def Pintar(self, boton):
        self.window.Draw(self.Fondo)
        self.PintarUsuarios()
        self.window.Draw(self.boton1)
        self.window.Draw(self.botonHome1)
        self.window.Draw(self.botonPrev1)
        self.window.Draw(self.botonNext1)
        if(boton == "SELECT"):
            self.window.Draw(self.boton2)
        if(boton == "HOME"):
            self.window.Draw(self.botonHome2)
        if(boton == "PREV"):
            self.window.Draw(self.botonPrev2)
        if(boton == "NEXT"):
            self.window.Draw(self.botonNext2)


    def BotonHovered(self, x, y):
        if(x>434 and x<791 and y>564 and y<664):
            return "SELECT"
        if(x>1115 and x<1200 and y>0 and y<80):
            return "HOME"
        if(x>0 and x<130 and y>200 and y<500):
            return "PREV"
        if(x>1070 and x<1200 and y>200 and y<500):
            return "NEXT"
    
    def Update(self):
        input = self.window.GetInput()
        self.DefinirFondo()
        self.DefinirBotones()
        self.DefinirUsuarios()
        self.DefinirSeleccionado()
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
                    self.UsuarioSeleccionado(x, y)
                    if(boton == "SELECT"):
                        self.BotonSelect()
                        self.BotonHome()
                        
                    if(boton == "HOME"):
                        self.BotonHome()

                    if(boton == "NEXT"):
                        self.SiguientesUsuarios()

                    if(boton == "PREV"):
                        self.AnterioresUsuarios()

                    
            self.window.Clear()
            self.Pintar(boton)
            self.window.Display()
        self.window.Close()
