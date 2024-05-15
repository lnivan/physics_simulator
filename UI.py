import pygame


class Vector2:
    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y
        self.mod = (x**2 + y**2)**(1/2)

    
    def __add__(self, other):

        result = Vector2(self.x + other.x, self.y + other.y)
        return(result)
    
    
    def __sub__(self, other):

        result = Vector2(self.x - other.x, self.y - other.y)
        return(result)
    
    
    def __mul__(self, other):

        if type(other) is Vector2:
            result = self.x * other.x + self.y + other.y
        
        else:
            result = Vector2(self.x * other, self.y * other)

        return(result)
    

    def __truediv__(self, other):

        result = Vector2(self.x / other, self.y / other)
        return(result)
    

    def unit(self):

        if self.mod != 0:
            result = self / self.mod

        else:
            result = Vector2(0, 1)

        return(result)
    
    def normal(self):

        result = Vector2(-self.y, self.x)
        return(result)
    

    def PygameVectorToVector2(PygameVector):
        
        result = Vector2(PygameVector[0], PygameVector[1])
        return(result)



class Button():

    def __init__(self, name, pos, size, func, ScreenSize):

        self.ScreenSize = ScreenSize
        self.name = name
        self.pos = pos
        self.size = size
        self.func = func
        self.MouseOver = False

    
    def Update(self, events):

        MousePos = Vector2.PygameVectorToVector2(pygame.mouse.get_pos())

        if self.pos.x < MousePos.x and MousePos.x < (self.pos.x + self.size.x):

            if self.ScreenSize[1] - self.pos.y > MousePos.y and MousePos.y > self.ScreenSize[1] - (self.pos.y + self.size.y):

                self.MouseOver = True

            else:

                self.MouseOver = False
        
        else:

            self.MouseOver = False

        for event in events:

            if self.MouseOver == True and event.type == pygame.MOUSEBUTTONUP:

                self.func("hola")




        


'''class Menu:

    def __init__(self):

        self.ButtonArray = []


    def AddButton(self, button):'''
