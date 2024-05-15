from draw import *
from physics import *
import pygame
import time


WindowSize = (800, 800)
window = Window(WindowSize)


class FPSCounter:

    def __init__(self):

        self.start = time.time()
        self.end = 0
        self.FPS = 0


    def Update(self):

        self.end = time.time()
        self.FPS = 1 / (self.end - self.start + 0.00001)
        self.start = time.time()


fps = FPSCounter()
        




sistem = System()




'''sistem.AddMassPoint("point1", Vector2(300, 300), 100)
sistem.AddMassPoint("point2", Vector2(500, 300), 100)
sistem.AddMassPoint("point3", Vector2(500, 500), 100)
sistem.AddMassPoint("point4", Vector2(300, 500), 100)
sistem.AddSpringJoint("spring1", "point1", "point2", 300, 10000)
sistem.AddSpringJoint("spring2", "point2", "point3", 300, 1000)
sistem.AddSpringJoint("spring3", "point3", "point4", 300, 1000)
sistem.AddSpringJoint("spring4", "point4", "point1", 300, 1000)
'''

'''sistem.AddMassPoint("point1", Vector2(400, 700), 10000, -30)
sistem.AddMassPoint("point2", Vector2(350, 700), 50, 1000)
sistem.AddMassPoint("point3", Vector2(300, 700), 50, 1000)
sistem.AddMassPoint("point4", Vector2(250, 700), 50, 1000)
sistem.AddMassPoint("point5", Vector2(200, 700), 50, 1000)
sistem.AddMassPoint("point6", Vector2(150, 700), 50, 1000)
sistem.AddMassPoint("point7", Vector2(100, 700), 50, 1000)
sistem.AddSpringJoint("spring1", "point1", "point2", 50, 10000)
sistem.AddSpringJoint("spring2", "point2", "point3", 50, 10000)
sistem.AddSpringJoint("spring3", "point3", "point4", 50, 10000)
sistem.AddSpringJoint("spring4", "point4", "point5", 50, 10000)
sistem.AddSpringJoint("spring5", "point5", "point6", 50, 10000)
sistem.AddSpringJoint("spring6", "point6", "point7", 50, 10000)'''

sistem.AddMassPoint("point1", Vector2(100, 400), 10000000, 0)
sistem.AddMassPoint("point2", Vector2(150, 400), 50, 1000)
sistem.AddMassPoint("point3", Vector2(200, 400), 50, 1000)
sistem.AddMassPoint("point4", Vector2(250, 400), 50, 1000)
sistem.AddMassPoint("point5", Vector2(300, 400), 50, 1000)
sistem.AddMassPoint("point6", Vector2(350, 400), 5000, 1000)
sistem.AddMassPoint("point7", Vector2(400, 400), 50, 1000)
sistem.AddMassPoint("point8", Vector2(450, 400), 50, 1000)
sistem.AddMassPoint("point9", Vector2(500, 400), 50, 1000)
sistem.AddMassPoint("point10", Vector2(550, 400), 50, 1000)
sistem.AddMassPoint("point11", Vector2(600, 400), 50, 1000)
sistem.AddMassPoint("point12", Vector2(650, 400), 50, 1000)
sistem.AddMassPoint("point13", Vector2(700, 400), 10000000, 0)

sistem.AddSpringJoint("spring1", "point1", "point2", 50, 50000)
sistem.AddSpringJoint("spring2", "point2", "point3", 50, 50000)
sistem.AddSpringJoint("spring3", "point3", "point4", 50, 50000)
sistem.AddSpringJoint("spring4", "point4", "point5", 50, 50000)
sistem.AddSpringJoint("spring5", "point5", "point6", 50, 50000)
sistem.AddSpringJoint("spring6", "point6", "point7", 50, 50000)
sistem.AddSpringJoint("spring7", "point7", "point8", 50, 50000)
sistem.AddSpringJoint("spring8", "point8", "point9", 50, 50000)
sistem.AddSpringJoint("spring9", "point9", "point10", 50, 50000)
sistem.AddSpringJoint("spring10", "point10", "point11", 50, 50000)
sistem.AddSpringJoint("spring11", "point11", "point12", 50, 50000)
sistem.AddSpringJoint("spring12", "point12", "point13", 50, 50000)



#sistem.AddMassPoint("point5", Vector2(500, 700), 100, 1000)




running = True
while running == True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    sistem.SimulateStep(0.001)

    window.WindowRefresh()
    window.DrawSystem(sistem)
    pygame.display.flip()


    fps.Update()
    print(fps.FPS)