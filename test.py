class Student():
    happy = 20
    def __init__(self, name, hieght = 160):
        self.name = name
        self.hieght = hieght
        Student.happy = 10
        self.happy = Student.happy
    def show(self):
        print(self.name, self.hieght, self.happy)


print()
st1 = Student("Bob", 185)
st2 = Student("Kat")
st3 = Student("Pit")

st1.show()
st2.show()
