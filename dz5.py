import random

class Robot_legs:
    def __init__(self):
        self.legsmemory = print('Ученые научили ходить робота. Робот прошел 10 шагов.')

class Robot_hands:
    def __init__(self):
        self.handsmemory = print('Ученые научили робота пользоваться руками. Робот собрал Дженгу.')
    
class Robot_AI:
    def __init__(self):
        self.logicsmemory = print('Ученые научили робота логике.')
    def __init__(self):
        self.interactionmemory = print('Благодаря интелекту робот смог овладеть частями тела.')
    
class Robot_1(Robot_legs, Robot_hands, Robot_AI):
    def info(self):
        print(self.legsmemory)
        print(self.handsmemory)
        print(self.logicsmemory)
        print(self.interactionmemory)
        


