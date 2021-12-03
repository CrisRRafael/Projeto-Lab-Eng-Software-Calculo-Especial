import unittest

from controller_calc_esp import CalcEspController

func = CalcEspController.calcular_raiz

class Test_calc(unittest.TestCase):

    def test_sub(self): 
        result =func("3,27")
        print(result)
        self.assertEqual(result, {'resultado':3.0})

if __name__ == '__main__':
    unittest.main()