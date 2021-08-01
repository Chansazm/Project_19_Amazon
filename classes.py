class strings:
    def __init__(self):
        self.items = "The letters"
        
    def print_items(self):
        print(self.items)
    

object = strings()
#object.print_items()

class Addition:
    first = 0
    second = 0
    answer = 0
    
    def __init__(self,f,s):
        self.first = f
        self.second = s
    
    def display(self):
        print("The first number is" + str(self.first))
        print("The second number is " + str(self.second))
        print("The answer is"+ str(self.answer))
    
    def calculate(self):
        self.answer = self.first + self.second
        
obj = Addition(5,8)
obj.calculate()
obj.display()
        
    