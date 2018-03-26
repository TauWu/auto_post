# 登录页面

from ..sele import *
from constant.logger import *

class PageLogin():

    def __init__(self, username):
        self.user = User()
        self.username, self.pwd, self.usertype = self.user.get_user_password(username)
        self.browser = None
        self.current_url = "http://vip.58ganji.com/login/"

    @property
    def login(self):

        if self.usertype == 1:
            '''安居客登录'''
            self.__login_base__("http://vip.58ganji.com/login/")
            self._login_ajk_

        elif self.usertype == 2:
            '''58登录'''
            self.__login_base__("http://vip.58ganji.com/thirdparty/58")
            self._login_58_
            time.sleep(2)
            
            to_url = self.__login_to_url__
            if to_url == 0:
                pass                    #登录成功直接交出浏览器对象
            elif to_url == 1:
                sele_info("用户[%s]实名认证没有完成，自动点击跳过..."%self.username)
                self.__skip_broker__    #跳过验证 登录成功交出浏览器对象
            elif to_url == 2:
                sele_info("用户[%s]首次在本台机器登录，需要输入验证码..."%self.username)
                self.__input_code__     #输入手机验证码
                self.__login_58_sub__   #重新登录

            sele_info("用户[%s]登录成功！"%self.username)
            return self.browser
    
    @property
    def __skip_broker__(self):
        broker_element = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.apply-link')))
        broker_element.click()

    @property
    def __login_to_url__(self):
        '''58登录完成后 会有三种跳转方式 将会一一验证'''
        current_url = self.browser.current_url

        # 需要实名验证
        if current_url == "http://vip.58ganji.com/broker/attest/":
            return 1

        # 需要验证手机号
        elif current_url.find("http://passport.58.com/warn/ui",0) != -1:
            return 2
        
        # 正常登录
        else:
            return 0

    def __login_base__(self, url):
        '''通过FireFox配置文件打开登录页面'''
        FireFoxDir = "/data/bin/user.login"
        try:
            profile = webdriver.FirefoxProfile(FireFoxDir)
            profile.native_events_enabled = True
            self.browser =  webdriver.Firefox(firefox_profile=profile)
            self.browser.get(url)
            self.browser.maximize_window()
        except Exception as e:
            sele_fatal("浏览器打开初始网页错误！")
            raise

    @property
    def _login_58_(self):
        '''从58登录开始登录'''
        self.__login_58_sub__

    @property
    def __login_58_sub__(self):
        browser = self.browser

        # 输入用户名等信息
        username_element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username_new')))
        password_element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password_new')))
        submit_btn = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#btnSubmit_new')))

        username_element.clear()
        username_element.send_keys(self.username)
        time.sleep(0.5)
        password_element.clear()
        password_element.send_keys(self.pwd)
        time.sleep(0.5)

        submit_btn.click()

        self.browser = browser

    @property
    def _login_ajk_(self):
        '''只有安居客的账号登录'''
        browser = self.browser

        # 输入用户名等信息
        username_element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginName")))
        password_element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginPwd")))
        submit_btn = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginSubmit")))

        username_element.clear()
        username_element.send_keys(self.username)
        time.sleep(0.5)
        password_element.clear()
        password_element.send_keys(self.pwd)
        time.sleep(0.5)

        self.browser = browser

        submit_btn.click()

    @property
    def __input_code__(self):
        browser_login = self.browser

        sms_btn = WebDriverWait(browser_login, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pptmobilecoderesendbtn")))
        sms_btn.click()

        sms_code = input("请输入接收到的验证码")
        sms_code_element = WebDriverWait(browser_login, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pptmobilecode')))
        sms_comfirm_btn = WebDriverWait(browser_login, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#submitButton')))
        
        sms_code_element.send_keys(sms_code)
        sms_comfirm_btn.click()

        self.browser = browser_login