import unittest
<<<<<<< HEAD
from calchan.tests.CalculatorHomeScreen import CalculatorMainHomeScreen
=======
from CalculatorFrameWork.tests.CalculatorHomeScreen import CalculatorMainHomeScreen
>>>>>>> 9a2f44cf64a28d3c1013b837a34b4673c38f3921


cmhs = unittest.TestLoader().loadTestsFromTestCase(CalculatorMainHomeScreen)
regressionTest = unittest.TestSuite([cmhs])
unittest.TextTestRunner(verbosity=1).run(regressionTest)


