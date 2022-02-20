class Cat():
    def __init__(self,name,color,height,mood,age):
        self.name=name
        self.color=color
        self.height=height
        self.mood=mood
        self.age=age
    
    def printattributes(self):
        print("name is",self.name)
        print("color is",self.color)
        print("height is",self.height)
        print("mood is",self.mood)
        print("age is",self.age)
cat1=Cat("riri","brown",37,"happy",5)
cat1.printattributes()