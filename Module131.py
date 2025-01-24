import asyncio

async def  start_strongman(name,power):
    print(f'Силач {name} начал гачислэм ')
    
    cumofballs = 5
    for ball in range(0, cumofballs ):
      delay = 1 / power
      await asyncio.sleep(delay)
      ball +=1
      print(f'Силач {name} поднял {ball} шаров ')  
    
    
    print(f'Силач {name} закончил гачислэм ') 
    
async def main():
  task1 = start_strongman('Van',3)
  task2 = start_strongman('billi',4)
  task3 = start_strongman('Buddy',5)
  await asyncio.gather(task1, task2, task3)
  
asyncio.run(main())