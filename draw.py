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



class Window:

    def __init__(self, size):

        self.size = size
        self.white = (255, 255, 255)
        self.gray = (100, 100, 100)
        self.black = (0, 0, 0)

        pygame.init()
        self.window = pygame.display.set_mode(self.size)

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 15)
        

    def WindowRefresh(self):

        self.window.fill(self.black)

    
    def DrawPoint(self, point):
        
        pos = point.R
        spos = (pos.x, self.size[1] - pos.y)
        
        pygame.draw.circle(self.window, self.white, spos, point.r)

    
    def DrawSpring(self, spring):

        start = spring.point1.R
        end = spring.point2.R

        p1Top2 = end - start
        p1Top2U = p1Top2.unit()
        p1Top2NU = p1Top2U.normal()
        
        StepN = int(spring.xn / 7)
        step = p1Top2 / StepN
        LinePoints = [(start.x, self.size[1] - start.y)]

        for i in range(1, StepN + 1):

            NewPoint = start + step * i + p1Top2NU * ((((i%2)-0.5)*2)*4)
            LinePoints.append((NewPoint.x, self.size[1] - NewPoint.y))
        
        pygame.draw.lines(self.window, self.white, False, LinePoints, 2)

    
    def DrawSystem(self, system):

        for point in system.MassPointDic.values():
            self.DrawPoint(point)

        for spring in system.SpringJointDic.values():
            self.DrawSpring(spring)


    def DrawButton(self, button):

        BGColor = self.white

        if button.MouseOver:

            BGColor = self.gray

        pos = (button.pos.x, self.size[1] - button.pos.y - button.size.y)
        size = (button.size.x, button.size.y)

        pygame.draw.rect(self.window, BGColor, pygame.Rect(pos, size))

        text = self.font.render(button.name, True, self.black)
        TextSize = text.get_size()
        TextPos = (button.pos.x + (button.size.x - TextSize[0]) / 2, self.size[1] - button.pos.y - button.size.y + (button.size.y - TextSize[1]) / 2)
        self.window.blit(text, TextPos)




        
        





        