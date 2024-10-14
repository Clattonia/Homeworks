class house:
    houses_history = []
    def __new__(cls,*args,**kwargs):
        obj = super(house, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return obj
    def __init__(self,name,floors):
        self.name = name
        self.floors = floors
        
        pass
    def __del__(self):
        print(f'{self.name} жил без страха, и умер без страха')
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
        return f'Название: {self.name}, Количество этажей: {self.floors}'
    def __lt__(self,other):
        return self.floors < other.floors #lt - меньше чем 
    
    def __add__(self,value):
        self.floors += value
        return  self #gt - меньше чем
    def __eq__(self,other):
        return self.floors == other.floors
      
    def __ne__(self, other):
      return self.floors != other.floors
    def __le__(self, other):
        return self.floors <= other.floors
    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = house("ВЫЖИВАТОР", 5)
print(house.houses_history)
h2 = house("МЕГАТОННА", 10) 
print(house.houses_history)
h3 = house("ГОРОДЗИЛА",20)
print(house.houses_history)

del h2
del h3

print(house.houses_history)