class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=None):
        
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        
        
        if step is None:
            step = -1 if start > stop else 1
        
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        
        self.pointer = self.start
        return self

    def __next__(self):
        
        if self.step > 0 and self.pointer >= self.stop:
            raise StopIteration
        
        if self.step < 0 and self.pointer <= self.stop:
            raise StopIteration
        
        
        current = self.pointer
        
        
        self.pointer += self.step
        
        return current


if __name__ == '__main__':
    
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')
    
    
    print("\nИтерация 2:")
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
    
    print("\nИтерация 3:")
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
    
    print("\nИтерация 4:")
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
    
    print("\nИтерация 5:")
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
        
        