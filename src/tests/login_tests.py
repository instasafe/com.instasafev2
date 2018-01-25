import logging
import time
import unittest
import pytest
from pages.loginPage import LoginPage
import utilities.custom_logger as cl
from utilities.teststatus import Status


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    
    
    _username = "gaurav"
    _password = "gaurav@123"

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_t1invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin with blank field")
        self.log.info("*#" * 20)
        self.lp.logout()
        time.sleep(3)
        self.lp.clickLoginButton()
        result1 = self.lp.verifyLoginFailed()
        assert result1 == False
    @pytest.mark.run(order=2)
    def test_t2invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t2invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with valid username and blank password field")
        self.lp.logout()
        self.lp.login("gaurav", "")
        result2 = self.lp.verifyLoginFailed()
        assert result2 == False
    @pytest.mark.run(order=3)
    def test_t3invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t3invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with blank username and valid password field")
        self.lp.logout()
        self.lp.login("", "gaurav@123")
        result3 = self.lp.verifyLoginFailed()
        assert result3 == False    

    @pytest.mark.run(order=4)
    def test_t4invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t4invalidLogin started")
        self.log.info("*#" * 20)
        self.log.info("test with valid username and blank password field")
        self.lp.logout()
        self.lp.login("test@email.com", "Abc@122")
        result4 = self.lp.verifyLoginFailed()
        assert result4 == False    
        
    @pytest.mark.run(order=5)
    def test_t5validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t5invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()        
        self.lp.login("gaurav", "gaurav@123")
        time.sleep(3)
        result5 = self.lp.verifyLoginTitle()
        self.ts.mark(result5, "Title Verification")
        result6 = self.lp.verifyLoginSuccessful()
        print("Result5: " + str(result5))
        print("Result6: " + str(result6))
        self.ts.markFinal("test_t5validLogin", result6, "Login Verification")