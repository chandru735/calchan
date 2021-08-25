from CalculatorFrameWork.base.BasePage import BasePage
import CalculatorFrameWork.utilities.CustomLogger as cl


class CalculatorHome(BasePage):  # extends here

    def __init__(self, driver):
        super().__init__(driver) # overiding since in basepage we have already initialised the page
        self.driver = driver



        # locator value inside calucaltor main page

    _privacypolicyagree = 'android:id/button1'  # id
    _privacypolicydisagree = 'android:id/button2'  # id
    _verifyagree = 'Agree' #test
    _verifydisagree = "Don't agree" #test
    _button1 = 'com.miui.calculator:id/btn_1_s'  # id
    _button2 = 'com.miui.calculator:id/btn_2_s'  # id
    _button3 = 'com.miui.calculator:id/btn_3_s'  # id
    _button4 = 'com.miui.calculator:id/btn_4_s'  # id
    _button5 = 'com.miui.calculator:id/btn_5_s'  # id
    _button6 = 'com.miui.calculator:id/btn_6_s'  # id
    _button7 = 'com.miui.calculator:id/btn_7_s'  # id
    _button8 = 'com.miui.calculator:id/btn_8_s'  # id
    _button9 = 'com.miui.calculator:id/btn_9_s'  # id
    _button0 = 'com.miui.calculator:id/btn_0_s'  # id
    _allclear = 'com.miui.calculator:id/btn_c_s'  # id
    _delete = 'com.miui.calculator:id/btn_del_s'  # id
    _percentile = 'com.miui.calculator:id/btn_percent_s'  # id
    _division = 'com.miui.calculator:id/btn_div_s'  # id
    _multiply = 'com.miui.calculator:id/btn_mul_s'  # id
    _minus = 'com.miui.calculator:id/btn_minus_s'  # id
    _addition = 'com.miui.calculator:id/btn_plus_s'  # id
    _defaultbuttonswitch = 'com.miui.calculator:id/btn_switch'  # id
    _dot = 'com.miui.calculator:id/btn_dot_s'  # id
    _equal = 'com.miui.calculator:id/btn_equal_s'  # id
    _minical = 'com.miui.calculator:id/ic_float_btn'  # id
    _directentry = 'com.miui.calculator:id/expression'  # id
    _calculatorhomescreen = 'com.miui.calculator:id/iv_tab_cal'  # id
    _coverter = 'com.miui.calculator:id/iv_tab_life'  # id
    _finance = 'com.miui.calculator:id/iv_tab_finance'  # id
    _settings = 'com.miui.calculator:id/ic_cal_more'  # id
    _settingshistory = 'com.miui.calculator:id/setting_history'  # id
    _settingsabout = 'com.miui.calculator:id/setting_about'  # id
    _buttonswitchmaxtomin = 'com.miui.calculator:id/btn_switch_s'  # id
    _eulersnumber = 'com.miui.calculator:id/btn_e'  # id
    _pi = 'com.miui.calculator:id/btn_pi'  # id
    _reciprocal = 'com.miui.calculator:id/btn_reciprocal'  # id
    _factorial = 'com.miui.calculator:id/btn_fac'  # id
    _squareroot = 'com.miui.calculator:id/btn_sqrt'  # id
    _power = 'com.miui.calculator:id/btn_pow'  # id
    _logarithm = 'com.miui.calculator:id/btn_lg'  # id
    _naturallogarithm = 'com.miui.calculator:id/btn_ln'  # id
    _leftparenthesis = 'com.miui.calculator:id/btn_lp'  # id
    _rightparenthesis = 'com.miui.calculator:id/btn_rp'  # id
    _secondfunctionswitch = 'com.miui.calculator:id/btn_2nd'  # id
    _angle = 'com.miui.calculator:id/btn_angle_or_rad'  # id
    _sine = 'com.miui.calculator:id/lyt_sin'  # id
    _cosine = 'com.miui.calculator:id/lyt_cos'  # id
    _tangent = 'com.miui.calculator:id/lyt_tan'  # id
    _listview = 'com.miui.calculator:id/listView' #id

    def clickprivacypolicyagree(self):
        self.clickElement(self._privacypolicyagree, 'id')
        cl.allureLogs('verified agree')

    def clickprivacypolicydisagree(self):
        self.clickElement(self._privacypolicydisagree,'id')
        cl.allureLogs('verified disagree')

    def verifyagreedisplayed(self):
        element = self.isDisplayed(self._verifyagree,"text")
        assert element == True

    def verifydisagreedisplayed(self):
        element = self.isDisplayed(self._verifydisagree,'text')
        assert element == True

    def clickbtn1(self):
        self.clickElement(self._button1,'id')
        cl.allureLogs('clicked on button 1')

    def clickbtn2(self):
        self.clickElement(self._button2,'id')
        cl.allureLogs('clicked on button 2')

    def clickbtn3(self):
        self.clickElement(self._button3,'id')
        cl.allureLogs('clicked on button 3')

    def clickbtn4(self):
        self.clickElement(self._button4,'id')
        cl.allureLogs('clicked on button 4')

    def clickbtn5(self):
        self.clickElement(self._button5,'id')
        cl.allureLogs('clicked on button 5')

    def clickbtn6(self):
        self.clickElement(self._button6,'id')
        cl.allureLogs('clicked on button 6')

    def clickbtn7(self):
        self.clickElement(self._button7,'id')
        cl.allureLogs('clicked on button 7')

    def clickbtn8(self):
        self.clickElement(self._button8,'id')
        cl.allureLogs('clicked on button 8')

    def clickbtn9(self):
        self.clickElement(self._button9,'id')
        cl.allureLogs('clicked on button 9')

    def clickbtn0(self):
        self.clickElement(self._button0,'id')
        cl.allureLogs('clicked on button 0')

    def clickallclear(self):
        self.clickElement(self._allclear,'id')
        cl.allureLogs('clicked all clear')

    def clickdelete(self):
        self.clickElement(self._delete,'id')
        cl.allureLogs('clicked on delete')

    def clickpercentage(self):
        self.clickElement(self._percentile,'id')
        cl.allureLogs('clicked on percentage')

    def clickdivision(self):
        self.clickElement(self._percentile,'id')
        cl.allureLogs('clicked on division')

    def clickmultiply(self):
        self.clickElement(self._multiply,'id')
        cl.allureLogs('clicked on multiply')

    def clickminus(self):
        self.clickElement(self._minus,'id')
        cl.allureLogs('clicked on minus')

    def clickaddition(self):
        self.clickElement(self._addition,'id')
        cl.allureLogs('clicked on addition')

    def clickdefaultbuttonswtich(self):
        self.clickElement(self._defaultbuttonswitch,'id')
        cl.allureLogs('clicked on default button switch')

    def clickdot(self):
        self.clickElement(self._dot,'id')
        cl.allureLogs('clicked on . button')

    def clickequal(self):
        self.clickElement(self._equal,'id')
        cl.allureLogs('clicked on equal button')

    def clickminical(self):
        self.clickElement(self._minical,'id')
        cl.allureLogs('clicked on mini calculator button')

    def clickuserentry(self):
        self.clickElement(self._directentry,'id')
        cl.allureLogs('clicked on user entry button')

    def clicktohomescreen(self):
        self.clickElement(self._calculatorhomescreen,'id')
        cl.allureLogs('clicked on homescreen button')

    def clickconverter(self):
        self.clickElement(self._coverter,'id')
        cl.allureLogs('clicked on converter button')

    def clickfinance(self):
        self.clickElement(self._finance,'id')
        cl.allureLogs('clicked on finance button')

    def clicksettings(self):
        self.clickElement(self._settings,'id')
        cl.allureLogs('clicked on settings button')

    def clicksettingshistory(self):
        self.clickElement(self._settingshistory,'id')
        cl.allureLogs('clicked on settings history button')

    def clicksettingsabout(self):
        self.clickElement(self._settingsabout,'id')
        cl.allureLogs('clicked on settings about button')

    def clicktoswitch(self):
        self.clickElement(self._buttonswitchmaxtomin,'id')
        cl.allureLogs('clicked on switch button')

    def clickeuler(self):
        self.clickElement(self._eulersnumber,'id')
        cl.allureLogs('clicked on euler button')

    def clickpi(self):
        self.clickElement(self._pi,'id')
        cl.allureLogs('clicked on pi button')

    def clickreciprocal(self):
        self.clickElement(self._reciprocal,'id')
        cl.allureLogs('clicked on reciprocal button')

    def clickfactorial(self):
        self.clickElement(self._factorial,'id')
        cl.allureLogs('clicked on factorial button')

    def clicksquareroot(self):
        self.clickElement(self._squareroot,'id')
        cl.allureLogs('clicked on squareroot button')

    def clickpower(self):
        self.clickElement(self._power,'id')
        cl.allureLogs('clicked on power button')

    def clicklogarithm(self):
        self.clickElement(self._logarithm,'id')
        cl.allureLogs('clicked on algorithm button')

    def clicknaturallogarithm(self):
        self.clickElement(self._naturallogarithm,'id')
        cl.allureLogs('clicked on natural algorithm button')

    def clickleftparenthesis(self):
        self.clickElement(self._leftparenthesis,'id')
        cl.allureLogs('clicked on left paranthesis button')

    def clickrightparenthesis(self):
        self.clickElement(self._rightparenthesis,'id')
        cl.allureLogs('clicked on right paranthesis button')

    def clickmaxsecondswitch(self):
        self.clickElement(self._secondfunctionswitch,'id')
        cl.allureLogs('clicked on max second switch')

    def clickangle(self):
        self.clickElement(self._angle,'id')
        cl.allureLogs('clicked on angle button')

    def clicksine(self):
        self.clickElement(self._sine,'id')
        cl.allureLogs('clicked on sine button')

    def clickcosine(self):
        self.clickElement(self._cosine,'id')
        cl.allureLogs('clicked on cosine button')

    def clicktangent(self):
        self.clickElement(self._tangent,'id')
        cl.allureLogs('clicked on tan button')

    def useSingleTap(self):
        self.singleTap(700,1990)
        cl.allureLogs(f'Single tapped on the coordinates')



