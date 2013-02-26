from PySFML import sf

class Sounds:
    def __init__(self):
        self.ALL_SOUNDS = []
        self.DIRECTORIO = "music/"
        self.MENU = "16.ogg"


    def PlayMenuMusic(self):
        self.menuMusic = self.PlayParam(self.DIRECTORIO+self.MENU, True)

    def PlayPlayingMusic(self):
        self.playingMusic = self.PlayParam(self.DIRECTORIO+self.PLAYING, True)

    def PlayGameOver(self):
        self.gover = self.PlayParam(self.DIRECTORIO+self.GAME_OVER, True)

    def StopGameOver(self):
        if self.gover != None:
            self.gover.Stop()

    def StopMenuMusic(self):
        if self.menuMusic != None:
            self.menuMusic.Stop()

    def StopPlayingMusic(self):
        if self.playingMusic != None:
            self.playingMusic.Stop()

    def StopGameOverMusic(self):
        if self.gover != None:
            self.gover.Stop()
        
    def PlayParam(self, path, loop):
        exp = sf.Music()
        exp.OpenFromFile(path)
        exp.Initialize(2, 44100)
        exp.SetLoop(loop)
        self.ALL_SOUNDS.append(exp)
        exp.Play()
        return exp

    def StopAll(self):
        for sound in self.ALL_SOUNDS:
            sound.Stop()


        
