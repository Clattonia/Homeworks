import threading
import time
class Knight(threading.Thread):
  frags = 100
  
  def __init__(self, name, power):
    threading.Thread.__init__(self, name=name)
    self.name = name
    self.power = power
    
  def run(self):
    print(f'{self.name}, на нас напали')
    frags = Knight.frags
    i=0
    while frags > 0:
        frags = frags - self.power
        print(f'{self.name} атакует! Осталось фрагов: {frags}')
        time.sleep(1)
        i += 1
    print(f'{self.name} одержал победу спустя {i} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Shinoko', 20)

first_knight.start()
second_knight.start()

