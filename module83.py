class IncorrectVinNumber(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)
        pass
class IncorrectCarNumber(Exception):
        def __init__(self, message):
          self.message = message
          super().__init__(self.message)
        pass
      
class Car:
    def __init__(self,model,vin,numbers) -> None:
      self.model = model
      if self.__is_valid_vin(vin):
          self.__vin = vin
      if self.__is_valid_numbers(numbers):
          self.__numbers = numbers
        
      pass
    
      
    def __is_valid_vin(self,vin):
        if not isinstance(vin, int):
          raise IncorrectVinNumber('Некоректный vin номер')
      
        if vin < 1000000 or vin > 9999999:
          raise IncorrectVinNumber('Некоректный vin номер')
        return True
    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumber('Некоректный тип данных')
        if len(numbers) > 6:
            raise IncorrectCarNumber('Неверная длина номера')
        return True
      
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')