from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from os.path import isfile, join
from os import listdir
from PySFML import sf

class Application:
    ready_to_delete = []
    activeWindow = None
    username = "NESTOR"
    @staticmethod
    def getFiles(directory):
        files = [ f for f in listdir(directory) if isfile(join(directory,f)) ]
        only_names = []
        for f in files:
            if (f.index(".xml") != -1):
                only_names.append( f[:f.index(".xml")])
                

        return only_names

    @staticmethod
    def deleteFile(directory):
        pass

    @staticmethod
    def existsFile(directory, filename):
        return (filename in Application.getFiles(directory))

    @staticmethod
    def getDirectories(directory):
        return [ f for f in listdir(directory) if not isfile(join(directory,f))]


    @staticmethod
    def createProfile(username, directory='profiles/'):
        if username == "" or username == None:
            return False
        treeP = ElementTree()
        root = Element("root")
        
        name = Element("name")
        name.text = username
        root.append(name)

        levels = Application.getDirectories("levels")
        for level_name in levels:
            nivel = Element("level")
            nivel.set("id", level_name)
            puzzles = Application.getFiles("levels/"+level_name)
            for puzzle in puzzles:
                if "_top" in puzzle:
                    continue
                pz = Element("puzzle")
                pz.set("id", puzzle)
                pz.text = "0"
                nivel.append(pz)
            root.append(nivel)
        treeP._setroot(root)
        treeP.write(directory+username+".xml")

        return True

    @staticmethod
    def createTopFile(directory, filename, top_n = 5):
        if filename == "" or filename == None:
            return False
        treeP = ElementTree()
        root = Element("top_scores")

        for i in range(top_n):
            top_i = Element("rank")
            top_i.set("user", "__EMPTY__")
            top_i.text = "0"
            root.append(top_i)
        treeP._setroot(root)
        treeP.write(directory+filename+".xml")
        return True

    @staticmethod
    def updateTopFile(directory, filename, user, score, top_n = 5):
        if not Application.existsFile(directory, filename):
            Application.createTopFile(directory, filename, top_n)

        pla = Application.getTopPlayers(directory, filename)
        t = [f for f in pla if f[0]==user and int(f[1])>score]
        if len(t) == 0:
            return False
        treeP = ElementTree()
        treeP.parse(directory+filename+".xml")
        root = treeP.getroot()
        new_root = Element("top_scores")
        ranks = root.findall("rank")
        top = min([top_n, len(ranks)])
        score_i = int(ranks[0].text)
        score_f = int(ranks[top-1].text)
        ins = False
        for i in range(top):
            if score <= int(ranks[i].text) or (ranks[i].attrib["user"] == "__EMPTY__"):
                tmp = Element("rank")
                tmp.set("user", user)
                tmp.text = str(score)
                new_root.append(tmp)
                ins = True
                break
            else:
                new_root.append(ranks[i])
        for j in range(i,top - 1):
            new_root.append(ranks[j])

        treeP2 = ElementTree()
        treeP2._setroot(new_root)

        treeP2.write(directory+filename+".xml")
        return ins

    @staticmethod
    def getTopScores(level, puzzle_number):
        try:
            tuplas = Application.getTopPlayers("levels/"+level+"/", str(puzzle_number)+"_top")
        except:
            Application.createTopFile("levels/"+level+"/", str(puzzle_number)+"_top")
        return Application.getTopPlayers("levels/"+level+"/",str(puzzle_number)+"_top")

    @staticmethod
    def getTopPlayers(directory, filename, top_n = 5):
        treeP = ElementTree()
        treeP.parse(directory + filename + ".xml")
        root = treeP.getroot()
        ranks = root.findall("rank")

        top_tuplas = []
        for rank in ranks:
            top_tuplas.append((rank.attrib["user"], rank.text))

        return top_tuplas

    @staticmethod
    def getScores(username, level):
        scores_tuplas = []
        treeP = ElementTree()
        treeP.parse("profiles/"+username+".xml")
        root = treeP.getroot()
        levels = root.findall("level")
        for level_ in levels:
            if level_.attrib["id"] == level:
                for i in level_.iter("puzzle"):
                    scores_tuplas.append((i.attrib["id"],i.text))
        return scores_tuplas

    @staticmethod
    def saveScore(username, level, puzzle, score):
        retVal = "NOT_FOUND"
        scores_tuplas = []
        treeP = ElementTree()
        treeP.parse("profiles/"+username+".xml")
        root = treeP.getroot()
        levels = root.findall("level")
        for level_ in levels:
            if level_.attrib["id"] == level:
                for i in level_.iter("puzzle"):
                    if i.attrib["id"] == str(puzzle):
                        if i.text == "0":
                            i.text = str(score)
                            retVal = "FIRST_TIME"
                        elif int(i.text)>int(score):
                            i.text = str(score)
                            retVal = "BETTER"
                        elif int(i.text)<int(score):
                            retVal = "NOT_BETTER"
                        else:
                            retVal = "EQUAL"
                break

        treeP.write("profiles/" + username + ".xml")
        return retVal

    @staticmethod
    def getNumberStacksLevel(level, numberLevel):
        treeP = ElementTree()
        treeP.parse("levels/"+level+"/"+numberLevel+".xml")
        root = treeP.getroot()
        levels = root.findall("nivel/stack")
        count = 0
        for level_ in levels:
            count=count+1
        return count

    @staticmethod
    def getNumberStacksSolution(level, numberLevel):
        treeP = ElementTree()
        treeP.parse("levels/"+level+"/"+numberLevel+".xml")
        root = treeP.getroot()
        levels = root.findall("solution/stack")
        count = 0
        for level_ in levels:
            count=count+1
        return count

    @staticmethod
    def getColorBoxFromStack(level, numberLevel, numberStack):
        scores_tuplas = []
        treeP = ElementTree()
        treeP.parse("levels/"+level+"/"+numberLevel+".xml")
        root = treeP.getroot()
        levels = root.findall("nivel/stack")
        count = 0
        for level_ in levels:
            if level_.attrib["id"] == str(numberStack):
                num = 1
                for i in level_.iter("caja"):
                     scores_tuplas.append((num, i.attrib["color"]))
                     num=num+1
        return scores_tuplas

    @staticmethod
    def getColorBoxFromStackSolution(level, numberLevel, numberStack):
        scores_tuplas = []
        treeP = ElementTree()
        treeP.parse("levels/"+level+"/"+numberLevel+".xml")
        root = treeP.getroot()
        levels = root.findall("solution/stack")
        count = 0
        for level_ in levels:
            if level_.attrib["id"] == str(numberStack):
                num = 1
                for i in level_.iter("caja"):
                     scores_tuplas.append((num, i.attrib["color"]))
                     num=num+1
        return scores_tuplas
           

    @staticmethod
    def getArmPosition(level, numberLevel):
        treeP = ElementTree()
        treeP.parse("levels/"+level+"/"+numberLevel+".xml")
        root = treeP.getroot()
        arm = root.find("nivel/arm")
        return int(arm.attrib["position"])
    
    @staticmethod
    def putOnDeleteList(item):
        Application.ready_to_delete.append(item)

    @staticmethod
    def destroyAnything():
        del Application.ready_to_delete[:]

    @staticmethod
    def getActiveWindow():
        return Application.activeWindow

    @staticmethod
    def setActiveWindow(window):
        Application.activeWindow = window

    @staticmethod
    def createSfSprite(path, x, y, w, h):
        image = sf.Image()
        image.LoadFromFile(path)
        sprite = sf.Sprite(image)
        sprite.Resize(w, h)
        sprite.SetCenter(0, 0)
        sprite.SetPosition(x, y)

        return sprite

if __name__ == "__main__":
    #pass
    Application.createTopFile("levels/GODMODE/","top_p1")
    Application.updateTopFile("levels/GODMODE/", "top_p1", "nestor", 100)
    Application.updateTopFile("levels/GODMODE/", "top_p1", "nestor", 97)
    #print Application.getTopPlayers("levels/GODMODE/", "top_p1")
