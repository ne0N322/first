import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 3
        self.moneydollar = 1000 #деньги студента
        self.physicalform = 100 #физическая форма студента
        self.alive = True
        self.day = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.alive:
            self.live(self.day)
            self.day += 1
            return f"Day {self.day}"
        elif self.day <= 366:
            raise StopIteration
    
    def to_study(self):
        print("Time to study")
        self.progress += 0.25
        self.gladness -= 5
        self.physicalform -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.physicalform -= 5
        self.moneydollar -= 80

    def to_money(self): #заработок денег 
        print("I need money")
        self.moneydollar += 400
        self.gladness -= 4
        self.progress -= 0.1
        self.physicalform += 2

    def to_meeting_friends(self): #студент гуляет с друзьями,девушкой или родственниками
        print("I want fun")
        self.moneydollar -= 130
        self.gladness += 2
        self.progress -= 0.2
    
    def to_physical_form(self): #студент занимается спортом
        print("I go to the gym")
        self.moneydollar -= 25
        self.physicalform += 7
        self.gladness += 1

    def to_self_development(self):  #студент саморазвивается
        print("I need more knowledge")
        self.gladness += 1
        self.progress += 0.10
        self.physicalform -= 1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False      #
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.moneydollar <= 0:
            print("I have no money...")
            self.alive = False  
        elif self.physicalform  <= 0:
            print("I can't move...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.moneydollar}")
        print(f"Physical form = {self.physicalform}")
    
    def live(self, day):
        day = " Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 7)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_money()
        elif live_cube == 5:
            self.to_meeting_friends()
        elif live_cube == 6:
            self.to_physical_form()
        elif live_cube == 7:
            self.to_self_development()
        #
        self.end_of_day()
        self.is_alive()
   
   
nick = Student(name="Nick")

for day in nick:
    pass

