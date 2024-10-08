class house:
    def __init__(self,name,floors):
        self.name = name
        self.floors = floors
        pass
    def go_to(self, new_floor):
        if new_floor > self.floors:
            print('Неправильно,попробуй еще раз')
        else:
            for i in range(new_floor):
                i += 1
                print(i)
    def __len__(self):
        return self.floors
    def __str__(self):
        return self.name
      

h1 = house("ЖК", 5)
h1.go_to(6)
print(len(h1))
print(str(h1))