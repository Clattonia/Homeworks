import unittest
from module123 import RunnerTest, TournamentTest

def skip_test_decorator(func):
    def wrapper(self, *args, **kwargs):
        if hasattr(self, 'is_frozen') and self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper


RunnerTest.is_frozen = False
TournamentTest.is_frozen = True


for name, method in RunnerTest.__dict__.items():
    if name.startswith('test_') and callable(method):
        setattr(RunnerTest, name, skip_test_decorator(method))

for name, method in TournamentTest.__dict__.items():
    if name.startswith('test_') and callable(method):
        setattr(TournamentTest, name, skip_test_decorator(method))


def create_test_suite():
    suite = unittest.TestSuite()
    
    
    suite.addTests(unittest. TestLoader() .loadTestsFromTestCase (RunnerTest))
    suite.addTests(unittest. TestLoader() .loadTestsFromTestCase (TournamentTest))
    
    
    return suite

# Create test runner
test_suite = create_test_suite()
test_runner = unittest.TextTestRunner(verbosity=2)

# Run the tests
if __name__ == '__main__':
    test_runner.run(test_suite)