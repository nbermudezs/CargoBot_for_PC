
import sys
import string
import random
import math
from PySFML import sf
from Application import Application
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element


class LevelEditor_Objects:

    
    def __init__(self):
        self.DIRECTORIO = "images/"
        self.DefinirSprites()

    def DefinirSprites(self):
        self.bgwidth = 65
        self.bgheight = 700 - 167
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/bg_toolbox.png")
        self.bg = sf.Sprite(image)
        self.bg.Resize(self.bgwidth, self.bgheight)
        self.bg.SetCenter(0, 0)
        self.bg.SetPosition(2, 167)

        posX_btns = 11
        self.btnwidth = 44
        width_btns = self.btnwidth
        height_btns = self.btnwidth
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/box_rojo.png")
        self.boxrojo = sf.Sprite(image)
        self.boxrojo.Resize(width_btns, height_btns)
        self.boxrojo.SetCenter(0, 0)
        self.boxrojo.SetPosition(posX_btns, 184)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/box_azul.png")
        self.boxazul = sf.Sprite(image)
        self.boxazul.Resize(width_btns, height_btns)
        self.boxazul.SetCenter(0, 0)
        self.boxazul.SetPosition(posX_btns, 249)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/box_verde.png")
        self.boxverde = sf.Sprite(image)
        self.boxverde.Resize(width_btns, height_btns)
        self.boxverde.SetCenter(0, 0)
        self.boxverde.SetPosition(posX_btns, 313)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/box_cafe.png")
        self.boxcafe = sf.Sprite(image)
        self.boxcafe.Resize(width_btns, height_btns)
        self.boxcafe.SetCenter(0, 0)
        self.boxcafe.SetPosition(posX_btns, 376)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/img_INS_CLEAR.png")
        self.botonClear = sf.Sprite(image)
        self.botonClear.Resize(width_btns, height_btns)
        self.botonClear.SetCenter(0, 0)
        self.botonClear.SetPosition(posX_btns, 442)
               
    def InstructionToolboxClicked(self, x, y):
        pos = self.bg.GetPosition()
        dim = (self.bgwidth, self.bgheight)
        if x<pos[0] or y<pos[1] or x>(dim[0] + pos[0]) or y>(dim[1] + pos[1]):
            return None
        else:
            pos = self.boxrojo.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "rojo"
            pos = self.boxazul.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "azul"
            pos = self.boxverde.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "verde"
            pos = self.boxcafe.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "cafe"
            pos = self.botonClear.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "INS_CLEAR"
            
    
    def Pintar(self, window):
        window.Draw(self.bg)
        window.Draw(self.boxrojo)
        window.Draw(self.boxverde)
        window.Draw(self.boxazul)
        window.Draw(self.boxcafe)
        window.Draw(self.botonClear)


"""
-------------------------------
Scenario + function set hicieron la fusion
"""


class Drawable_Scenario:
    def __init__(self, xi, yi, xf, yf, final):
        #self.puzzle_number = puzzle_number
       # self.level_name = level_name        
        self.DIRECTORIO = "images/"
        self.there_is_arm = False
        self.goal = None
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.final = final
        
        self.btnwidth = 44
        
        self.num_stacks = 8 #Application.getNumberStacksLevel(level_name, puzzle_number)
        stack_desp = (8 - self.num_stacks)/2
        self.scale_x = (xf - xi)/1200.0
        self.scale_y = (yf - yi)/700.0
        self.stack_desp = stack_desp 
        self.stacks = []
        self.i=1      
        
        #for i in range(self.num_stacks):
        self.stacks.append(Drawable_Stack(0,self.scale_x, [xi, yi, xf, yf], final, stack_desp))
      #  self.stacks.append(Drawable_Stack(self.num_stacks,self.scale_x, [self.xi, self.yi, self.xf, self.yf], final, stack_desp))
        
        
        #imagenes
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/scenario_bg_top.png")
        self.bg = sf.Sprite(image)
        self.bg.Resize(xf - xi, 651 - yi)
        self.bg.SetCenter(0, 0)
        self.bg.SetPosition(xi, yi)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/scenario_bg_bottom.png")
        self.bg_bot = sf.Sprite(image)
        self.bg_bot.Resize(xf - xi, yf - 650)
        self.bg_bot.SetCenter(0, 0)
        self.bg_bot.SetPosition(xi, 650)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/pole.png")
        self.poleL = sf.Sprite(image)
        self.poleL.Resize(30, yf - yi)
        self.poleL.SetCenter(0, 0)
        self.poleL.SetPosition(xi, yi)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/pole.png")
        self.poleR = sf.Sprite(image)
        self.poleR.Resize(30, yf - yi)
        self.poleR.SetCenter(0, 0)
        self.poleR.SetPosition(xf - 30, yi)
        if not final:
            self.BuildArm([xi, yi, xf, yf])

    def BuildArm(self, boundaries):
        self.there_is_arm = True
        self.armPos = 1 #Application.getArmPosition(self.level_name, self.puzzle_number)
        self.initial_arm_pos = self.armPos
        self.arm = Drawable_Arm(self.armPos, self.scale_x, self.num_stacks, boundaries, self.stack_desp)

    def ResetConfigs(self):
        for stack in self.stacks:
            stack.ResetConfigs()
        if self.there_is_arm:
            self.arm.ResetConfigs()
            self.arm.SetPosition(self.initial_arm_pos)

    def GetStack(self, pos):
        if len(self.stacks)<= pos-1 or (pos <1):
            return None
        return self.stacks[pos - 1]

    def CompareScenarios(self, scenario):
        identical = True
        for i in range(len(self.stacks)):
            identical = (identical and self.stacks[i].CompareStack(scenario.stacks[i]))
        return identical


    def addStack(self):
        if(self.i < 8):
            stack_desp = (8 - self.num_stacks)/2
            self.stack_desp = stack_desp
          
            self.stacks.append(Drawable_Stack(self.i,self.scale_x, [self.xi, self.yi, self.xf, self.yf], self.final, stack_desp))
            
            self.i += 1

    def deleteStack(self,cual):
        Application.putOnDeleteList(self.stacks[cual])
        del self.stacks[cual]
        self.i-= 1

        x=cual
        while( x< len(self.stacks)):
            self.stacks[x].Reposition(x)
            x+=1
           
            
           

    def Clear(self):
        x=1
        
        length = len(self.stacks)
        while x < length:
            del self.stacks[1]
            x+=1
            
        
        length = len(self.stacks[0].stack)
        x=0
        while x < length:
            del self.stacks[0].stack[0]
            x+=1
            
            
        self.i =1
            
    def Update(self, frameTime):
        return self.arm.Update(frameTime)

    def Ejecutar(self, function_set):
        self.arm.Ejecutar(function_set, self)

    def RunNextStep(self, function_set):
        self.arm.NextStep(function_set, self)

    def DetenerEjecucion(self):
        self.arm.DetenerEjecucion()

    def GetBoxSize(self):
        for i in self.stacks:
            if len(i.stack) != 0:
                return i.stack[0].box.GetSubRect().GetHeight()*i.stack[0].box.GetScale()[0]
        return 80*self.scale_x

    def PlaceBox(self,stack, box):

        if(len(self.stacks)>stack):
            scenario_boundaries = [self.xi, self.yi, self.xf, self.yf]
            stack_boundaries = [(120 + 110*(1+self.stack_desp) + 15)*self.scale_x + scenario_boundaries[0], 650,
                                (120 + 110*(1+self.stack_desp) + 15)*self.scale_x + scenario_boundaries[0] + 90*self.scale_x, 650 + 30*self.scale_x]
        
       
            #if box[0] <=8:

            #newlen =
            arraybox = [len(self.stacks[stack].stack),box]
            print arraybox
            
            itembox = Drawable_Box(stack,arraybox,stack_boundaries,self.scale_x,stack)
            #self.stacks.append(itembox)
            self.stacks[stack].InsertOnTop(itembox)
            
            
    def BoxClicked(self, x, y, stack):

        
        box = self.getBoxClicked(x,y,self.stacks[stack])
        
        #print (["cajita",box.id,box.color])

        temp = box

        del self.stacks[stack].stack[box.id]

        
        
        return (temp.box,temp.color)
        """
        res = self.PlaceInstruction(x, y)
        if res[0] == False:
            return False
        if self.functions[res[1]].instructions[res[2]] != None:
            ins_type = self.functions[res[1]].instructions[res[2]].type
            self.functions[res[1]].RemoveInstruction(res[2])
            ref.SetDraggingInstruction(ins_type)
            return True
        return False
        """
    
    def Pintar(self, window):
        window.Draw(self.bg)
        window.Draw(self.bg_bot)
        #window.Draw(self.poleL)
        #window.Draw(self.poleR)
        for stack in self.stacks:
            stack.Pintar(window)
        if self.there_is_arm:
            self.arm.Pintar(window)

    def getBoxClicked(self,x,y,stack):

        
        for box in stack.stack:
            pos = []
            pos = box.GetPosition()
            lol = (self.btnwidth + pos[0],self.btnwidth + pos[1])
            if x>pos[0] and y>pos[1] and x<lol[0] and y<lol[1]:
                box.SetPerfectPosition(len(stack.stack))
                return box
    
        

"""
---------------------------
Drawable stack
"""
class Drawable_Stack:

    def __init__(self, stack_id, scale, scenario_boundaries, final, stack_desp):
        self.DIRECTORIO = "images/"
        self.stack_id = stack_id
      #  self.level_name = level_name
       # self.puzzle_number = puzzle_number
        self.scenario_boundaries = scenario_boundaries
        self.final = final
        self.stack_desp = stack_desp
        self.scale = scale
        self.stack = []

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/base.png")
        self.base = sf.Sprite(image)
        self.base.Resize(90*scale, 30*scale)
        self.base.SetCenter(0, 0)
        self.base.SetPosition((120 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0],650)

        self.stack_boundaries = [(120 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0], 650,
                                (120 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0] + 90*scale, 650 + 30*scale]
      #  self.setInitialState(stack_id, scale, scenario_boundaries, final, stack_desp)


    def setInitialState(self, stack_id,scale, scenario_boundaries, final, stack_desp):
        if final:
            boxes = Application.getColorBoxFromStackSolution(level_name, puzzle_number, stack_id+1)
        else:
            boxes = Application.getColorBoxFromStack(level_name, puzzle_number, stack_id+1)
        
        self.stack_boundaries = [(120 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0], 650,
                                (120 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0] + 90*scale, 650 + 30*scale]

        for box in boxes:
            self.stack.append(Drawable_Box(stack_id, box, stack_boundaries, scale, len(boxes)))

        self.scale = scale
        self.stack_boundaries = stack_boundaries

    def Reposition(self, stack_id):
        self.stack_id = stack_id
        self.stack_boundaries = [(120 + 110*(stack_id+self.stack_desp) + 15)*self.scale + self.scenario_boundaries[0], 650,
                                (120 + 110*(stack_id+self.stack_desp) + 15)*self.scale + self.scenario_boundaries[0] + 90*self.scale, 650 + 30*self.scale]
        
        self.base.SetPosition((120 + 110*(stack_id+self.stack_desp) + 15)*self.scale + self.scenario_boundaries[0],650)
        for box in self.stack:
            box.Reposition(self.stack_boundaries)
            
            
    def ResetConfigs(self):
        while len(self.stack)>0:
            Application.putOnDeleteList(self.stack.pop())
        self.setInitialState(self.stack_id, self.level_name, self.puzzle_number, self.scale, self.scenario_boundaries, self.final, self.stack_desp)

    def Pintar(self, window):
        window.Draw(self.base)
        for box in self.stack:
            box.Pintar(window)

    def Collides(self, pos_y):
        if len(self.stack) == 0:
            return False
        box = self.stack[0]
        rect = sf.FloatRect(box.box.GetPosition()[0], box.box.GetPosition()[1],
                          box.box.GetPosition()[0] + box.box.GetSize()[0], box.box.GetPosition()[1] + box.box.GetSize()[1])
        return rect.Contains((rect.Left + rect.Right)/2, pos_y)

    def CollidesX(self, pos_x):
        if len(self.stack) == 0:
            return False
        box = self.stack[0]
        rect = sf.FloatRect(box.box.GetPosition()[0], box.box.GetPosition()[1],
                          box.box.GetPosition()[0] + box.box.GetSize()[0], box.box.GetPosition()[1] + box.box.GetSize()[1])
        return rect.Contains(pos_x, (rect.Top + rect.Bottom)/2)

    def Adjust(self, minim, maxim):
        if len(self.stack) == 0:
            return 0
        i1 = 0
        while self.CollidesX(minim):
            self.stack[0].Move(1, 0)
            i1 = 1
        i2 = 0
        while self.CollidesX(maxim):
            if i1 == 1:
                self.stack[0].Move(-1,0)
                return 2
            self.stack[0].Move(-1, 0)
            i2 = 1
        return i1+i2

    def InsertOnTop(self, box):
        box.stack_id = self.stack_id
      #  print(self.stack_id)
        box.stack_boundaries = self.stack_boundaries
        box.SetPerfectPosition(len(self.stack))
        self.stack.insert(0, box)
    
    def CompareStack(self, stack):
        if len(self.stack)!=len(stack.stack):
            return False
        identical = True
        for i in range(len(self.stack)):
            identical = identical and self.stack[i].Equals(stack.stack[i])

        return identical

"""
---------------------------------
Drawable arm
"""

class Drawable_Arm:
    def __init__(self, initial_position, scale, num_stacks, scenario_boundaries, stack_desp):
        self.DIRECTORIO = "images/"
        self.estado = "IDLE"
        self.stack_desp = stack_desp
        self.scenario_boundaries = scenario_boundaries
        self.scale = scale
        self.moving = False
        self.direction = None
        self.scenario = None
        self.function_set = None
        self.velocity = 255
        self.function_id = 0
        self.instruction_id = 0
        self.ticksResuelto = 0
        self.termino_instruction = True
        self.currentPos = initial_position
        self.initial_pos = initial_position
        self.catching = False
        self.catching2 = False
        self.movingUp = False
        self.movingDown = False
        self.resuelto = False

        self.attachedBox = None

        rscale_x = 145/283.0*self.scale
        rscale_y = 125/313.0*self.scale
        x0 = (160 + 110*(initial_position + self.stack_desp - 1) - 15)*self.scale + self.scenario_boundaries[0]
        y0 = self.scenario_boundaries[1] + 1
        
        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/arm/cable.png")
        self.cable = sf.Sprite(image)
        self.cable.Resize(44*rscale_x, 65*rscale_y + 4)
        self.base_cable_size = (44*rscale_x, 65*rscale_y + 4)
        self.cable_height = self.base_cable_size[1]
        self.cable.SetCenter(0, 0)
        self.cable.SetPosition(x0 + (145*self.scale - rscale_x*44)/2.0, y0 - 4)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/arm/holder.png")
        self.holder = sf.Sprite(image)
        self.holder.Resize(230*rscale_x, 72*rscale_y)
        self.holder.SetCenter(0, 0)
        self.holder.SetPosition(x0 + 26*rscale_x, y0 + 65*rscale_y)
        self.base_holder_size = (230*rscale_x, 72*rscale_y)

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/arm/left_pin.png")
        self.left_pin = sf.Sprite(image)
        self.left_pin.Resize(53*rscale_x, 176*rscale_y)
        self.left_pin.SetCenter(0, 0)
        self.left_pin.SetPosition(x0, y0 + 65*rscale_y + 72*rscale_y)
        self.base_left_pin_pos = (x0, y0 + 65*rscale_y + 72*rscale_y)
        self.base_left_pin_size = (53*rscale_x, 176*rscale_y)

        self.ddx = 26*rscale_x

        image = sf.Image()
        image.LoadFromFile(self.DIRECTORIO+"gameplay/arm/right_pin.png")
        self.right_pin = sf.Sprite(image)
        self.right_pin.Resize(53*rscale_x, 176*rscale_y)
        self.right_pin.SetCenter(0, 0)
        self.right_pin.SetPosition(x0 + 145*self.scale - 53*rscale_x, y0 + 65*rscale_y + 72*rscale_y)
        self.base_right_pin_pos = (x0 + 145*self.scale - 53*rscale_x, y0 + 65*rscale_y + 72*rscale_y)
        self.base_right_pin_size = (53*rscale_x, 176*rscale_y)

    def SetPosition(self, initial_position):
        rscale_x = 145/283.0*self.scale
        rscale_y = 125/313.0*self.scale
        x0 = (160 + 110*(initial_position + self.stack_desp - 1) - 15)*self.scale + self.scenario_boundaries[0]
        y0 = self.scenario_boundaries[1] + 1

        self.cable.SetPosition(x0 + (145*self.scale - rscale_x*44)/2.0, y0 - 4)
        self.holder.SetPosition(x0 + 26*rscale_x, y0 + 65*rscale_y)
        self.left_pin.SetPosition(x0, y0 + 65*rscale_y + 72*rscale_y)
        self.right_pin.SetPosition(x0 + 145*self.scale - 53*rscale_x, y0 + 65*rscale_y + 72*rscale_y)

    def SetVelocity(self, velocity):
        self.velocity = velocity

    def GetStackPosition(self, pos):
        return (160 + 110*(pos + self.stack_desp - 1) - 15)*self.scale + self.scenario_boundaries[0]        

    def ResetConfigs(self):
        self.cable_height = self.base_cable_size[1]
        self.cable.Resize(self.base_cable_size[0], self.base_cable_size[1])
        if self.attachedBox != None:
            Application.putOnDeleteList(self.attachedBox)
            self.attachedBox = None

    def MoverHorizontal(self, des):
        self.cable.Move(des, 0)
        self.holder.Move(des, 0)
        self.left_pin.Move(des, 0)
        self.right_pin.Move(des, 0)
        if self.attachedBox != None:
            self.attachedBox.box.Move(des, 0)

    def MoverVertical(self, des):
        if self.movingDown:
            stack = self.scenario.GetStack(self.currentPos)
            if stack == None:
                return
            self.collides = stack.Collides(self.holder.GetPosition()[1] + self.holder.GetSize()[1] + 6)
            if not self.collides:
                self.holder.Move(0, des)
                self.left_pin.Move(0, des)
                self.right_pin.Move(0, des)
                self.cable_height += des
                self.cable.Resize(self.base_cable_size[0], self.cable_height)
            else:
                self.movingDown = False
                self.catching = True
        if self.movingUp:
            if self.cable_height + des < self.base_cable_size[1]:
                des = self.base_cable_size[1] - self.cable_height
            self.holder.Move(0, des)
            self.left_pin.Move(0, des)
            self.right_pin.Move(0, des)
            self.cable_height += des
            self.cable.Resize(self.base_cable_size[0], self.cable_height)
            
        if self.catching:
            if not self.collides:
                if not self.catching2:
                    l = self.left_pin.GetSize()[0] + self.left_pin.GetPosition()[0]
                    r = self.right_pin.GetPosition()[0]
                    if l < r:
                        self.left_pin.Move(des/6, 0)
                        self.right_pin.Move(-des/6,0)
                    else:
                        self.catching2 = True
                else:
                    if self.holder.GetPosition()[0] - self.ddx < self.left_pin.GetPosition()[0]:                        
                        self.left_pin.Move(-des/2, 0)
                        self.right_pin.Move(des/2, 0)
                    else:
                        self.left_pin.SetPosition(self.holder.GetPosition()[0] - self.ddx, self.left_pin.GetPosition()[1])
                        self.right_pin.SetPosition(self.holder.GetPosition()[0] + self.holder.GetSize()[0] - self.ddx, self.left_pin.GetPosition()[1])
                        self.catching = False
                        self.catching2 = False
                        self.movingUp = True
            else:
                
                if not self.catching2:
                    l = self.left_pin.GetSize()[0] + self.left_pin.GetPosition()[0]
                    r = self.right_pin.GetPosition()[0]
                    c = self.scenario.GetStack(self.currentPos).Adjust(l, r)
                    if l < r and c != 2:
                        self.left_pin.Move(des/6, 0)
                        self.right_pin.Move(-des/6,0)
                        #if self.left_pin.GetSize()[0] + self.left_pin.GetPosition()[0] > self.right_pin.GetPosition()[0]:
                        #    self.left_pin.SetPosition(self.base_left_pin_pos[0], self.left_pin.GetPosition()[1])
                    else:
                        self.catching2 = True
                else:
                    self.catching = False
                    self.catching2 = False
                    self.movingUp = True
                    self.attachedBox = self.scenario.GetStack(self.currentPos).stack.pop(0)
            

    def Ejecutar(self, function_set, scenario):
        self.collides = False
        self.playingStepByStep = False
        self.stepDone = True
        if self.function_set == None:
            self.function_set = function_set
        if self.scenario == None:
            self.scenario = scenario
        self.moving = True
        #self.function_id = 0
        #self.instruction_id = 0

    def NextStep(self, function_set, scenario):
        if self.moving:
            return
        if self.function_set == None:
            self.function_set = function_set
        if self.scenario == None:
            self.scenario = scenario
        self.stepDone = False
        self.playingStepByStep = True  
        self.moving = True

    def StopStepByStep(self):
        if self.playingStepByStep:
            self.moving = False
            self.stepDone = True

    def DetenerEjecucion(self):
        self.currentPos = self.initial_pos
        self.moving = False
        self.movingDown = False
        self.movingUp = False
        self.catching = False
        self.termino_instruction = True
        self.function_id = 0
        self.instruction_id = 0

    def Update(self, frameTime):
        if self.resuelto:
            self.ticksResuelto += frameTime
            return True
            if self.ticksResuelto >= 100:
                return True
            else:
                return
        if self.moving:            
            if self.termino_instruction:
                if self.playingStepByStep and self.stepDone:
                    return
                if self.function_set != None:
                    self.resuelto = self.scenario.CompareScenarios(self.scenario.goal)
                    print ("RESUELTO?: " +str(self.resuelto))
                    self.termino_instruction = False                    
                    self.direction = self.function_set.GetInstruction(self.function_id, self.instruction_id)
                    self.function_set.SetHighlightInstruction(self.function_id, self.instruction_id)
                    self.instruction_id += 1
                    if self.direction == "INS_DOWN":
                        self.movingDown = True
            else:                
                if self.direction == "INS_DOWN":
                    if self.movingDown:
                        if self.attachedBox == None:
                            limit = 595
                        else:
                            limit = 590 - len(self.scenario.GetStack(self.currentPos).stack)*self.scenario.GetBoxSize()
                        if self.holder.GetPosition()[1] >= limit:
                            if self.attachedBox == None: #llego al fondo sin caja!
                                self.movingDown = False
                                self.catching = True
                                self.movingUp = False
                            else: #llego al lugar donde poner la caja que carga!
                                self.scenario.GetStack(self.currentPos).InsertOnTop(self.attachedBox)
                                self.attachedBox = None
                                self.movingDown = False
                                self.movingUp = False
                                self.catching = True
                                self.catching2 = True
                                
                        else: #  aun no ha llego lo mas bajo que puede llegar                          
                            desp_x = frameTime*self.velocity
                            self.MoverVertical(desp_x)
                            if self.attachedBox != None:
                                posy = self.holder.GetPosition()[1] + self.base_holder_size[1]
                                self.attachedBox.SetPositionY(posy)
                    elif self.movingUp:
                        if int(self.holder.GetPosition()[1]) <= self.base_cable_size[1] + self.cable.GetPosition()[1]:
                            self.movingDown = False
                            self.catching = False
                            self.movingUp = False
                            self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                            self.termino_instruction = True
                            self.StopStepByStep()
                        else:
                            desp_x = -frameTime*self.velocity
                            self.MoverVertical(desp_x)
                            if self.attachedBox != None:
                                posy = self.holder.GetPosition()[1] + self.base_holder_size[1]
                                self.attachedBox.SetPositionY(posy)
                    elif self.catching or self.catching2:
                        self.MoverVertical(frameTime*self.velocity)
                    
                elif self.direction == "PROG_1":
                    self.function_id = 0
                    self.instruction_id = 0
                    self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                    self.termino_instruction = True
                    self.StopStepByStep()
                elif self.direction == "PROG_2":
                    self.function_id = 1
                    self.instruction_id = 0
                    self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                    self.termino_instruction = True
                    self.StopStepByStep()
                elif self.direction == "PROG_3":
                    self.function_id = 2
                    self.instruction_id = 0
                    self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                    self.termino_instruction = True
                    self.StopStepByStep()
                elif self.direction == "PROG_4":
                    self.function_id = 3
                    self.instruction_id = 0
                    self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                    self.termino_instruction = True
                    self.StopStepByStep()
                elif self.direction == "INS_RIGHT":
                    stack = self.scenario.GetStack(self.currentPos + 1)
                    if stack == None:
                        return
                    if self.left_pin.GetPosition()[0] >= self.GetStackPosition(self.currentPos + 1):
                        x = self.left_pin.GetSize()[0]/2;
                        self.base_left_pin_pos = (self.GetStackPosition(self.currentPos + 1) + x, self.left_pin.GetPosition()[1])
                        self.currentPos += 1
                        self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                        self.termino_instruction = True
                        self.StopStepByStep()
                    else:
                        desp_x = frameTime*self.velocity
                        self.MoverHorizontal(desp_x)
                elif self.direction == "INS_LEFT":
                    stack = self.scenario.GetStack(self.currentPos - 1)
                    if stack == None:
                        print ("ERROR!!")
                        return
                    if self.left_pin.GetPosition()[0] <= self.GetStackPosition(self.currentPos - 1):
                        self.base_left_pin_pos = (self.GetStackPosition(self.currentPos - 1) + self.left_pin.GetSize()[0]/2, self.left_pin.GetPosition()[1])
                        self.currentPos -= 1
                        self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
                        self.termino_instruction = True
                        self.StopStepByStep()
                        
                    else:
                        desp_x = -frameTime*self.velocity
                        self.MoverHorizontal(desp_x)
                elif self.direction == None:
                    self.termino_instruction = True
                    self.StopStepByStep()
            
    
    def Pintar(self, window):
        window.Draw(self.cable)
        window.Draw(self.holder)
        window.Draw(self.left_pin)
        window.Draw(self.right_pin)
        if self.attachedBox != None:
            self.attachedBox.Pintar(window)

   
    
"""
----------------
drawable box
"""
class Drawable_Box:

    def __init__(self, stack_id, box, stack_boundaries, scale, tot):
        self.stack_boundaries = stack_boundaries
        self.stack_id = stack_id
        self.scale = scale
        self.id = box[0]
        self.color = box[1]
        self.DIRECTORIO = "images/gameplay/"
        self.DefinirBox(stack_id, box, scale, tot)
        self.pos = 0
    def DefinirBox(self, stack_id, box, scale, tot):
        rand_desp = random.randrange(int(-5*scale), int(5*scale))
        self.box = Application.createSfSprite(self.DIRECTORIO+"box_"+self.color+".png",
                                              self.stack_boundaries[0] + 5*scale + rand_desp,
                                              self.stack_boundaries[1] - math.ceil(80*scale*(tot - self.id + 1)),
                                              80*scale, 80*scale)

    def SetPerfectPosition(self, pos):
        rand_desp = random.randrange(int(-5*self.scale), int(5*self.scale))
        self.box.SetPosition(self.stack_boundaries[0] + 5*self.scale + rand_desp, 
                             self.stack_boundaries[1] - math.ceil(80*self.scale*(pos + 1)))
        self.pos = pos

    def Reposition(self,stack_boundaries):
        rand_desp = random.randrange(int(-5*self.scale), int(5*self.scale))
        self.box.SetPosition(stack_boundaries[0] + 5*self.scale + rand_desp, 
                             stack_boundaries[1] - math.ceil(80*self.scale*(self.pos + 1)))
        
    def Pintar(self, window):
        window.Draw(self.box)

    def Move(self, dx, dy):
        self.box.Move(dx, dy)

    def SetPositionY(self, posy):
        self.box.SetPosition(self.box.GetPosition()[0], posy)

    def Equals(self, box):
        #return (self.id == box.id and self.color == box.color)
        return self.color == box.color

    def SetPosition(self,x,y):
        self.box.SetPosition(x,y)
        
    def GetPosition(self):
        return self.box.GetPosition()


#############################################

class GenerarXML:

    def __init__(self):
        pass
    
    def Generar(self,scene,goal):
        root = Element('root')
        nivel = Element('nivel')
        solution = Element('solution')

        arm = Element('arm',{'position':str(scene.armPos)})

        
        nivel.append(arm)

        for stack in scene.stacks:
            elstack = Element('stack', {'id':str(stack.stack_id+1)})
            for box in stack.stack:
                elbox = Element('caja',{'color':box.color})
                elstack.append(elbox)
            nivel.append(elstack)

        for stack in goal.stacks:
            elstack = Element('stack', {'id':str(stack.stack_id+1)})
            for box in stack.stack:
                elbox = Element('caja',{'color':box.color})
                elstack.append(elbox)
            solution.append(elstack)    
            
        root.append(nivel)
        root.append(solution)

        ElementTree(root).write('levels\LEVELEDITOR\customtest.xml')
        #s = tostring(goal)
        
     
        
        
        

    
