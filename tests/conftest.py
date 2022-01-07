import pytest
import time
<<<<<<< HEAD
from calchan.base.DriverClass import Driver
=======
from CalculatorFrameWork.base.DriverClass import Driver
>>>>>>> 9a2f44cf64a28d3c1013b837a34b4673c38f3921


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')