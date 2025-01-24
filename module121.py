import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 100000

    def __str__(self):
        return self.name
      
      
class RunnerTest(unittest.TestCase,Runner):
    def testWalk(self):
      runer = Runner("TestRunner")
      for _ in range(10):
            runer.walk()
        
        # Проверяем значение distance
      self.assertEqual(runer.distance, 50)

    def testRun(self):
          runer = Runner("TestRunner")
          for _ in range(10):
                runer.run()
            
            # Проверяем значение distance
          self.assertEqual(runer.distance, 100)
    def test_challenge(self):
          runer = Runner("TestRunner")
          for _ in range(10):
                runer.run()
                runer.walk()
            
            # Проверяем значение distance
          self.assertNotEqual(runer.run(), 100)
if __name__ == '__main__':
    unittest.main()