from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['app'] = ('D:\learning\APk\com.miui.calculator_12.3.16.apk')
        desired_caps['appPackage'] = 'com.miui.calculator'
        desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'
        desired_caps['deviceName'] = 'Mi 11 Ultra'
        desired_caps["appWaitForLaunch"] = False
        desired_caps["autoGrantPermissions"] = True

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver