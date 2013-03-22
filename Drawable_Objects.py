import sys
import string
import random
import math
import time
from PySFML import sf
from Application import Application

class Drawable_Scenario:
    def __init__(self, xi, yi, xf, yf, level_name, puzzle_number, final):
        self.puzzle_number = puzzle_number
        self.level_name = level_name        
        self.DIRECTORIO = "images/gameplay/"
        self.there_is_arm = False
        self.goal = None
        self.final = final

        self.num_stacks = Application.getNumberStacksLevel(level_name, puzzle_number)
        stack_desp = (8 - self.num_stacks)/2
        self.scale_x = (xf - xi)/1200.0
        self.scale_y = (yf - yi)/700.0
        self.stack_desp = stack_desp 
        self.stacks = []
        
        for i in range(self.num_stacks):
            self.stacks.append(Drawable_Stack(i, level_name, puzzle_number,self.scale_x, [xi, yi, xf, yf], final, stack_desp))

        #imagenes
        self.filter = Application.createSfSprite(self.DIRECTORIO+"scenario_filter.png", xi, yi, xf - xi, yf - yi)
        self.bg = Application.createSfSprite(self.DIRECTORIO+"scenario_bg2.png", xi, yi, xf - xi, yf - yi)

        #self.bg_bot = Application.createSfSprite(self.DIRECTORIO+"scenario_bg_bottom.png", xi, 650, xf - xi, yf - 650)

        #self.poleL = Application.createSfSprite(self.DIRECTORIO+"pole.png", xi, yi, 30, yf - yi)

        #self.poleR = Application.createSfSprite(self.DIRECTORIO+"pole.png", xf - 30, yi, 30, yf - yi)
        if not final:
            self.BuildArm([xi, yi, xf, yf])

    def BuildArm(self, boundaries):
        self.there_is_arm = True
        self.armPos = Application.getArmPosition(self.level_name, self.puzzle_number)
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

    def SetVelocity(self, velo):
        if self.there_is_arm:
            self.arm.SetVelocity(velo)

    def Pintar(self, window):
        #if self.final:
        #    window.Draw(self.filter)
        #else:
        #    window.Draw(self.bg)
        #window.Draw(self.bg_bot)
        #window.Draw(self.poleL)
        #window.Draw(self.poleR)
        for stack in self.stacks:
            stack.Pintar(window)
        if self.there_is_arm:
            self.arm.Pintar(window)

"""
FIN CLASS DRAWABLE_SCENARIO
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_STACK
"""

class Drawable_Stack:

    def __init__(self, stack_id, level_name, puzzle_number, scale, scenario_boundaries, final, stack_desp):
        self.DIRECTORIO = "images/gameplay/"
        self.stack_id = stack_id
        self.level_name = level_name
        self.puzzle_number = puzzle_number
        self.scenario_boundaries = scenario_boundaries
        self.final = final
        self.stack_desp = stack_desp
        self.stack = []

        self.base = Application.createSfSprite(self.DIRECTORIO+"base.png",
                                               (160 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0],650,
                                               90*scale, 30*scale)
        
        self.setInitialState(stack_id, level_name, puzzle_number, scale, scenario_boundaries, final, stack_desp)


    def setInitialState(self, stack_id, level_name, puzzle_number, scale, scenario_boundaries, final, stack_desp):
        if final:
            boxes = Application.getColorBoxFromStackSolution(level_name, puzzle_number, stack_id+1)
        else:
            boxes = Application.getColorBoxFromStack(level_name, puzzle_number, stack_id+1)
        
        stack_boundaries = [(160 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0], 650,
                            (160 + 110*(stack_id+stack_desp) + 15)*scale + scenario_boundaries[0] + 90*scale, 650 + 30*scale]

        for box in boxes:
            self.stack.append(Drawable_Box(stack_id, box, stack_boundaries, scale, len(boxes)))

        self.scale = scale
        self.stack_boundaries = stack_boundaries

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

    def IsFull(self):
        return len(self.stack) == 6

    def InsertOnTop(self, box):
        box.stack_id = self.stack_id
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
FIN CLASS DRAWABLE_STACK
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_BOX
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

    def Pintar(self, window):
        window.Draw(self.box)

    def Move(self, dx, dy):
        self.box.Move(dx, dy)

    def SetPositionY(self, posy):
        self.box.SetPosition(self.box.GetPosition()[0], posy)

    def Equals(self, box):
        #return (self.id == box.id and self.color == box.color)
        return self.color == box.color


"""
FIN CLASS DRAWABLE_BOX
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_ARM
"""

class Drawable_Arm:
    def __init__(self, initial_position, scale, num_stacks, scenario_boundaries, stack_desp):
        self.DIRECTORIO = "images/gameplay/arm/"
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
        self.ERROR = False
        self.returnPoints = []

        self.attachedBox = None

        rscale_x = 145/283.0*self.scale
        rscale_y = 125/313.0*self.scale
        x0 = (160 + 110*(initial_position + self.stack_desp - 1) - 15)*self.scale + self.scenario_boundaries[0]
        y0 = self.scenario_boundaries[1] + 1

        self.cable = Application.createSfSprite(self.DIRECTORIO+"cable.png",
                                                x0 + (145*self.scale - rscale_x*44)/2.0, y0 - 4,
                                                44*rscale_x, 65*rscale_y + 4)

        self.base_cable_size = (44*rscale_x, 65*rscale_y + 4)
        self.cable_height = self.base_cable_size[1]

        self.holder = Application.createSfSprite(self.DIRECTORIO+"holder.png",
                                                 x0 + 26*rscale_x, y0 + 65*rscale_y,
                                                 230*rscale_x, 72*rscale_y)
        
        self.base_holder_size = (230*rscale_x, 72*rscale_y) 

        self.left_pin = Application.createSfSprite(self.DIRECTORIO+"left_pin.png",
                                                   x0, y0 + 65*rscale_y + 72*rscale_y,
                                                   53*rscale_x, 176*rscale_y)
        
        self.base_left_pin_pos = (x0, y0 + 65*rscale_y + 72*rscale_y)
        self.base_left_pin_size = (53*rscale_x, 176*rscale_y)

        self.ddx = 26*rscale_x

        self.right_pin = Application.createSfSprite(self.DIRECTORIO+"right_pin.png",
                                                    x0 + 145*self.scale - 53*rscale_x, y0 + 65*rscale_y + 72*rscale_y,
                                                    53*rscale_x, 176*rscale_y)
        
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

    def MoverVerticalDown(self, des):
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

    def MoverVerticalUp(self, des):
        if self.movingUp:
            if self.cable_height + des < self.base_cable_size[1]:
                des = self.base_cable_size[1] - self.cable_height
            self.holder.Move(0, des)
            self.left_pin.Move(0, des)
            self.right_pin.Move(0, des)
            self.cable_height += des
            self.cable.Resize(self.base_cable_size[0], self.cable_height)

    def MoverVerticalCatching(self, des):
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

    def MoverVertical(self, des):
        self.MoverVerticalDown(des)
        self.MoverVerticalUp(des)
        self.MoverVerticalCatching(des)
               

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
        self.ERROR = False
        self.termino_instruction = True
        self.function_id = 0
        self.instruction_id = 0

    def HaSidoResuelto(self, frameTime):
        if self.resuelto:
            self.ticksResuelto += frameTime
            return True
            if self.ticksResuelto >= 100:
                return True
            else:
                return False
        return False

    def SiguienteInstruccion(self):
        if self.function_set != None:
            self.resuelto = self.scenario.CompareScenarios(self.scenario.goal)
            self.termino_instruction = False
            last_pos = self.function_set.GetPosLastInstruction(self.function_id)
            if last_pos == -1 or last_pos < self.instruction_id:
                if len(self.returnPoints)>0:
                    tup = self.returnPoints.pop()
                    self.function_id = tup[0]
                    self.instruction_id = tup[1]
                
            direction = self.function_set.GetInstruction(self.function_id, self.instruction_id)
            self.function_set.SetHighlightInstruction(self.function_id, self.instruction_id)
            self.instruction_id += 1
            if direction == "INS_DOWN":
                self.movingDown = True
            elif (direction in ["PROG_1", "PROG_2", "PROG_3", "PROG_4"]):
                self.returnPoints.append((self.function_id, self.instruction_id))
            return direction

    def CambiarAProg(self, prog_id):
        self.function_id = prog_id
        self.instruction_id = 0
        self.function_set.UnsetHighlightInstruction(self.function_id, self.instruction_id)
        self.termino_instruction = True
        self.StopStepByStep()
        time.sleep(0.15)

    def BuildErrorMessage(self):
        x = Drawable_Message("ERROR_1", "mensaje")
        return x

    def Update(self, frameTime):
        if self.HaSidoResuelto(frameTime):
            return True
        if self.ERROR:
            return False
        if self.moving:            
            if self.termino_instruction:
                if self.playingStepByStep and self.stepDone:
                    return
                stack = self.scenario.GetStack(self.currentPos)
                
                self.direction = self.SiguienteInstruccion()
                if stack != None and self.direction != None:
                    if stack.IsFull() and self.direction == "INS_DOWN" and self.attachedBox != None:
                        window = Application.getActiveWindow()
                        window.SetMessage(self.BuildErrorMessage())
                        self.ERROR = True
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
                    self.CambiarAProg(0)
                elif self.direction == "PROG_2":
                    self.CambiarAProg(1)
                elif self.direction == "PROG_3":
                    self.CambiarAProg(2)
                elif self.direction == "PROG_4":
                    self.CambiarAProg(3)
                elif self.direction == "INS_RIGHT":
                    stack = self.scenario.GetStack(self.currentPos + 1)
                    if stack == None:
                        self.ERROR = True
                        window = Application.getActiveWindow()
                        window.SetMessage(self.BuildErrorMessage())
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
                        self.ERROR = True
                        window = Application.getActiveWindow()
                        window.SetMessage(self.BuildErrorMessage())
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
FIN CLASS DRAWABLE_ARM
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_SLIDER
"""

class Drawable_Slider:
    def __init__(self, xi, yi, xf, yf, default_value):
        self.current = default_value
        self.clicked = False
        self.DIRECTORIO = "images/gameplay/slider/"
        r_width = 768
        r_height = 133
        scale_x = 356.0/768.0
        scale_y = 45.0/143.0
         
        self.piece = Application.createSfSprite(self.DIRECTORIO+"piece.png", xi, yi - 10, (xf - xi)*(2.03/13.0), yf - yi + 9)
        self.fixed = Application.createSfSprite(self.DIRECTORIO+"fixed.png", xi, yi + (1.02/2.27)*(yf - yi), xf - xi, (yf - yi)*(1.25/2.27))

    def GetVelocity(self):
        return self.current

    def HasFocus(self, x, y):
        a = x>=self.fixed.GetPosition()[0]
        c = x<=self.fixed.GetPosition()[0] + self.fixed.GetSize()[0] - self.piece.GetSize()[0]
        return a and c

    def InRange(self, x, y):
        a = x>=self.fixed.GetPosition()[0]
        b = y>=self.piece.GetPosition()[1]
        c = x<=self.fixed.GetPosition()[0] + self.fixed.GetSize()[0] #- self.piece.GetSize()[0]
        d = y<=self.piece.GetPosition()[1] + self.piece.GetSize()[1]
        return a and b and c and d

    def Update(self, frameTime, evento, x, y):
        if evento.Type == sf.Event.MouseButtonPressed:            
            if not self.InRange(x, y):
                return False
            self.clicked = True
            
        if self.clicked:
            if evento.Type == sf.Event.MouseButtonReleased:
                p = self.piece.GetPosition()[0] - self.fixed.GetPosition()[0] + self.piece.GetSize()[0]
                self.current = 50 + 350*(p/self.fixed.GetSize()[0])
                self.clicked = False
                return True
            
            if self.HasFocus(x, y):
                self.piece.SetPosition(x, self.piece.GetPosition()[1])
                return False
            else:
                if x > self.fixed.GetPosition()[0] + self.fixed.GetSize()[0] - self.piece.GetSize()[0]:
                    self.piece.SetPosition(self.fixed.GetPosition()[0] + self.fixed.GetSize()[0] - self.piece.GetSize()[0], self.piece.GetPosition()[1])
                elif x < self.fixed.GetPosition()[0]:
                    self.piece.SetPosition(self.fixed.GetPosition()[0], self.piece.GetPosition()[1])
            
        
            

    def Pintar(self, window):
        window.Draw(self.fixed)
        window.Draw(self.piece)        

"""
FIN CLASS DRAWABLE_SLIDER
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_FUNCTION
"""

class Drawable_Function:

    def __init__(self, function_id, x, y):
        self.DIRECTORIO = "images/gameplay/"
        self.function_id = function_id
        self.instructions = []
        for i in range(8):
            self.instructions.append(None)

        self.DefinirSprites(x, y)

    def DefinirSprites(self, x, y):
        self.height = 44
        self.empty = Application.createSfSprite(self.DIRECTORIO+"empty_instruction_set_"+str(self.function_id)+".png", x, y, 433, 46)

    def InsertInstruction(self, pos, instruction):
        if self.instructions[pos] != None:
            return False
        import random
        rot = random.randrange(-3, 3)
        instruction.SetRotation(rot)
        self.instructions[pos] = instruction
        return True

    def GetInstruction(self, ins_id):
        if ins_id >= len(self.instructions):
            return None
        else:
            if self.instructions[ins_id] == None:
                return None
            return self.instructions[ins_id].GetType()

    def GetPosLastInstruction(self):
        pos = -1
        for i in range(len(self.instructions)):
            if self.instructions[i] != None:
                pos = i
        return pos

    def GetCount(self):
        c = 0
        for i in self.instructions:
            if i != None:
                c += 1
        return c

    def GetSprite(self, ins_id):
        if ins_id >= len(self.instructions):
            return None
        else:
            if self.instructions[ins_id] == None:
                return None
            return self.instructions[ins_id].GetSprite()

    def HighLight(self, ins_id):
        if ins_id >= len(self.instructions):
            return 
        else:
            if self.instructions[ins_id] == None:
                return 
            self.instructions[ins_id].HighLight()

    def UnHighLight(self, ins_id):
        if ins_id >= len(self.instructions):
            return 
        else:
            if self.instructions[ins_id] == None:
                return 
            self.instructions[ins_id].UnHighLight()

    def RemoveInstruction(self, pos):
        Application.putOnDeleteList(self.instructions[pos])
        self.instructions[pos] = None

    def VerticalDistance(self, y):
        pos = self.empty.GetPosition()
        if y>pos[1] and y<pos[1] + self.height:
            return 0
        if y>pos[1]:
            return y - pos[1] - self.height
        if y<=pos[1]:
            return pos[1] - y

    def Clear(self):
        for i in range(len(self.instructions)):
            self.RemoveInstruction(i)
            

    def GetHorizontalIndex(self, x):
        size = (516 - 125)/8
        for i in range(8):
            if x<125+(i+1)*size and x>125+i*size:
                return i
        return -1

    def Pintar(self, window):
        window.Draw(self.empty)
        for instruction in self.instructions:
            if instruction != None:
                instruction.Pintar(window)

"""
FIN CLASS DRAWABLE_FUNCTION
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_FUNCTIONSET
"""


class Drawable_FunctionSet:
    def __init__(self):
        self.highlight_fid = None
        self.highlight_iid = None
        self.functions = []

        function = Drawable_Function(1, 76, 166)
        self.functions.append(function)

        function = Drawable_Function(2, 76, 246)
        self.functions.append(function)

        function = Drawable_Function(3, 76, 326)
        self.functions.append(function)

        function = Drawable_Function(4, 76, 406)
        self.functions.append(function)

    def Pintar(self, window):
        for function in self.functions:
            function.Pintar(window)

    def Clear(self):
        for func in self.functions:
            func.Clear()


    def GetCount(self):
        c = 0
        for f in self.functions:
            c += f.GetCount()
        return c

    def GetInstruction(self, function_id, instruction_id):
        if function_id >= len(self.functions):
            return None
        else:
            return self.functions[function_id].GetInstruction(instruction_id)

    def GetPosLastInstruction(self, function_id):
        if function_id >= len(self.functions):
            return -1
        else:
            return self.functions[function_id].GetPosLastInstruction()

    def ResetConfigs(self):
        if self.highlight_fid != None and self.highlight_iid != None:
            self.UnsetHighlightInstruction(self.highlight_fid, self.highlight_iid)
            self.highlight_fid = None
            self.highlight_iid = None

    def PlaceInstruction(self, x, y):
        if x>518 or x<76:
            return [False]
        distances = [function.VerticalDistance(y) for function in self.functions]
        minim = min(distances)
        if minim > 21:
            return [False]
        for i in range(len(distances)):
            if distances[i] == minim:
                break
        index = self.functions[i].GetHorizontalIndex(x)
        if index == -1:
            return [False]
        else:
            if self.functions[i].instructions[index] == None:
                return [True, i, index]
            else:
                return [True, i, index, self.functions[i].instructions[index].type]

    def SetHighlightInstruction(self, funct_id, instr_id):
        self.highlight_fid = funct_id
        self.highlight_iid = instr_id
        if funct_id >= len(self.functions):
            return
        if self.functions[funct_id].GetInstruction(instr_id) == None:
            return
        self.oldSize = self.functions[funct_id].GetSprite(instr_id).GetSize()
        self.oldPos = self.functions[funct_id].GetSprite(instr_id).GetPosition()
        self.functions[funct_id].GetSprite(instr_id).Resize(self.oldSize[0]*1.2, self.oldSize[1]*1.2)
        self.functions[funct_id].GetSprite(instr_id).SetPosition(self.oldPos[0] - 4, self.oldPos[1] - 4)
        self.functions[funct_id].HighLight(instr_id)

    def UnsetHighlightInstruction(self, funct_id, instr_id):
        if self.highlight_fid == None:
            return
        if self.highlight_fid >= len(self.functions):
            return
        if self.functions[self.highlight_fid].GetInstruction(self.highlight_iid) == None:
            return
        self.functions[self.highlight_fid].GetSprite(self.highlight_iid).Resize(self.oldSize[0], self.oldSize[1])
        self.functions[self.highlight_fid].GetSprite(self.highlight_iid).SetPosition(self.oldPos[0], self.oldPos[1])
        self.functions[self.highlight_fid].UnHighLight(self.highlight_iid)

    def InsertInstruction(self, function_id, instr_id, sprite, instr_type):
        di = Drawable_Instruction(function_id, instr_id, sprite, instr_type)
        return self.functions[function_id].InsertInstruction(instr_id, di)

    def InstructionClicked(self, x, y, ref):
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
FIN CLASS DRAWABLE_FUNCTIONSET
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_INSTRUCTION
"""

class Drawable_Instruction:

    def __init__(self, function_id, pos, sprite, instr_type):
        self.type = instr_type
        self.sprite = sprite
        size = (516 - 125)/8
        self.sprite.SetPosition(131+pos*size, 169+80*function_id)
        self.highligth = False

    def SetRotation(self, rotation):
        self.sprite.SetRotation(rotation)

    def GetSprite(self):
        return self.sprite

    def GetType(self):
        return self.type

    def Pintar(self, window):
        window.Draw(self.sprite)

    def HighLight(self):
        self.higlight = True
        image = sf.Image()
        image.LoadFromFile("images/gameplay/img_" + self.type + "_2.png")
        self.sprite.SetImage(image)

    def UnHighLight(self):
        self.higlight = False
        image = sf.Image()
        image.LoadFromFile("images/gameplay/img_" + self.type + ".png")
        self.sprite.SetImage(image)

"""
FIN CLASS DRAWABLE_INSTRUCTION
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_TOOLBOX
"""

class Drawable_Toolbox:

    def __init__(self):
        self.DIRECTORIO = "images/gameplay/"
        self.DefinirSprites()

    def DefinirSprites(self):
        self.bgwidth = 65
        self.bgheight = 700 - 167
        posX_btns = 11
        self.btnwidth = 44
        width_btns = self.btnwidth
        height_btns = self.btnwidth

        self.bg = Application.createSfSprite(self.DIRECTORIO+"bg_toolbox.png", 0, 167, self.bgwidth, self.bgheight)        

        self.botonDown = Application.createSfSprite(self.DIRECTORIO+"img_INS_DOWN.png", posX_btns, 184, width_btns, height_btns)

        self.botonRight = Application.createSfSprite(self.DIRECTORIO+"img_INS_RIGHT.png", posX_btns, 249, width_btns, height_btns)

        self.botonLeft = Application.createSfSprite(self.DIRECTORIO+"img_INS_LEFT.png", posX_btns, 313, width_btns, height_btns)

        self.botonProg1 = Application.createSfSprite(self.DIRECTORIO+"img_PROG_1.png", posX_btns, 376, width_btns, height_btns)

        self.botonProg2 = Application.createSfSprite(self.DIRECTORIO+"img_PROG_2.png", posX_btns, 442, width_btns, height_btns)

        self.botonProg3 = Application.createSfSprite(self.DIRECTORIO+"img_PROG_3.png", posX_btns, 506, width_btns, height_btns)

        self.botonProg4 = Application.createSfSprite(self.DIRECTORIO+"img_PROG_4.png", posX_btns, 569, width_btns, height_btns)

        self.botonClear = Application.createSfSprite(self.DIRECTORIO+"img_INS_CLEAR_2.png", posX_btns, 634, width_btns, height_btns)

    def DisableClear(self):
        img = sf.Image()
        img.LoadFromFile(self.DIRECTORIO+"img_INS_CLEAR_2.png")
        self.botonClear.SetImage(img)

    def EnableClear(self):
        img = sf.Image()
        img.LoadFromFile(self.DIRECTORIO+"img_INS_CLEAR.png")
        self.botonClear.SetImage(img)
        
    def InstructionToolboxClicked(self, x, y):
        pos = self.bg.GetPosition()
        dim = (self.bgwidth, self.bgheight)
        if x<pos[0] or y<pos[1] or x>(dim[0] + pos[0]) or y>(dim[1] + pos[1]):
            return None
        else:
            pos = self.botonDown.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "INS_DOWN"
            pos = self.botonRight.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "INS_RIGHT"
            pos = self.botonLeft.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "INS_LEFT"
            pos = self.botonProg1.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "PROG_1"
            pos = self.botonProg2.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "PROG_2"
            pos = self.botonProg3.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "PROG_3"
            pos = self.botonProg4.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "PROG_4"
            pos = self.botonClear.GetPosition()
            if x>pos[0] and y>pos[1] and x<(pos[0] + self.btnwidth) and y<(pos[1] + self.btnwidth):
                return "INS_CLEAR"
            
    
    def Pintar(self, window):
        window.Draw(self.bg)
        window.Draw(self.botonDown)
        window.Draw(self.botonLeft)
        window.Draw(self.botonRight)
        window.Draw(self.botonProg1)
        window.Draw(self.botonProg2)
        window.Draw(self.botonProg3)
        window.Draw(self.botonProg4)
        window.Draw(self.botonClear)


"""
FIN CLASS DRAWABLE_TOOLBOX
---------------------------------------------------------------------
INICIO CLASS DRAWABLE_MESSAGE
"""

class Drawable_Message:

    def __init__(self, tipo, mensaje):
        self.errorCount = 4
        self.DIRECTORIO = "images/errors/"
        self.fade = Application.createSfSprite(self.DIRECTORIO + "fade.png", 0, 0, 0, 0)
        if tipo in ["ERROR_1", "ERROR_2"]:
            self.DefinirMensaje(tipo, 0, 0, 350, 200)
        else:
            self.DefinirMensaje(tipo)
        self.DefinirSprites()

    def DefinirMensaje(self, tipo, x = 0, y = 0, w = 0, h = 0):
        tipo = "ERROR_" + str(random.randint(0,self.errorCount - 1))
        self.mensaje  = Application.createSfSprite(self.DIRECTORIO + tipo + ".png", x, y, w, h)

    def DefinirSprites(self):
        x = self.mensaje.GetPosition()[0] - 5
        y = self.mensaje.GetPosition()[1] - 5
        w = self.mensaje.GetSize()[0] + 10
        h = self.mensaje.GetSize()[1] + 10
        self.bg = Application.createSfSprite(self.DIRECTORIO+"bg.png", x, y, w, h)        
        
    def ButtonClicked(self, x, y):
        pass

    def Update(self, window):
        wt = window.GetWidth()
        ht = window.GetHeight()
        w = self.mensaje.GetSize()[0]
        h = self.mensaje.GetSize()[1]
        self.fade.Resize(wt, ht)
        self.bg.SetPosition((wt - w)/2, (ht - h)/2)
        self.mensaje.SetPosition((wt - w)/2 + 5, (ht - h)/2 + 5)
    
    def Pintar(self, window):
        #print ("tratando de pintarse!")
        self.Update(window)
        window.Draw(self.fade)
        window.Draw(self.bg)
        window.Draw(self.mensaje)
        #window.Draw(self.botonOK)
