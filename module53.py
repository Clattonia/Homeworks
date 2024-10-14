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
h2 = house("МЕГАТОННА", 10)
print(h1)
print(h2)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
