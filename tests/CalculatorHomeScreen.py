import unittest

import pytest

from CalculatorFrameWork.base.DriverClass import Driver
import CalculatorFrameWork.utilities.CustomLogger as cl
from CalculatorFrameWork.base.BasePage import BasePage
from CalculatorFrameWork.pages.CalculatorHomeScreenPage import CalculatorHome

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class CalculatorMainHomeScreen(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = CalculatorHome(self.driver)

    @pytest.mark.run(order=1)
    def test_C248996468(self):
        cl.allureLogs('App Launched')
        self.cf.verifyagreedisplayed()
        self.cf.verifydisagreedisplayed()
        self.cf.clickprivacypolicyagree()
        self.cf.clickbtn2()
        self.cf.clickbtn1()
        self.cf.clickbtn0()
        self.cf.clickbtn8()
        self.cf.clickaddition()
        self.cf.clickbtn9()
        self.cf.clickbtn7()
        self.cf.clickminus()
        self.cf.clickbtn4()
        self.cf.clickmultiply()
        self.cf.clickbtn3()
        self.cf.clickdivision()
        self.cf.clickbtn5()
        self.cf.clickequal()
        self.cf.clickdefaultbuttonswtich()
        self.cf.clickdelete()
        self.cf.clicksine()
        self.cf.clicksettings()
        self.cf.useSingleTap()
        self.cf.clickfinance()














