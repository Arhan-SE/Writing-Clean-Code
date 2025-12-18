class Math:
    def __init__(self, num_1, num_2):
        self.is_add=True
        self.num_1=num_1
        self.num_2=num_2

class Add(Math):
    def __init__(self, num_1, num_2, num_3):
        super().__init__(num_1, num_2)
        self.num_3=num_3
    def add(self):
        return self.num_1 + self.num_2 + self.num_3
    
num_1 = 2
num_2 = 4
num_3 = 5
instance=Add(num_1=num_1, num_2=num_2, num_3=num_3)

print(instance.add())