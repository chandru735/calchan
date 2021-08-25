import unittest
from CalculatorFrameWork.tests.CalculatorHomeScreen import CalculatorMainHomeScreen


cmhs = unittest.TestLoader().loadTestsFromTestCase(CalculatorMainHomeScreen)
regressionTest = unittest.TestSuite([cmhs])
unittest.TextTestRunner(verbosity=1).run(regressionTest)


