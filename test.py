import unittest 

def check(x):

    return x >= 100

class MyTest(unittest.TestCase):

        def test(self):
            self.assertTrue (check(200))
            

if __name__== '__main__':

    unittest.main()