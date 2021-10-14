class School:
    def __init__(self,name,roll,mark):
        self.name = name
        self.roll = roll
        self.mark = mark
    def Add(self):
        c = []
        a = input("name")
        b = input("roll")
        c = input("marks")
        d = School(a,b,c)
        c.append(d)
        
x = School("c",5,6)
x.Add()