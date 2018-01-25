import logging
import time

from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl


class LoginPage(BasePage,SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
       

    # Locators
    # _login_link = ".//input[@class='form-control ng-pristine ng-valid ng-empty ng-touched']"
    _username_Field = ".//input[@placeholder='Username']"
    _password_field = ".//input[@placeholder='Password']"
    _login_button = ".//button[@class='btn theme-purple-btn']"

    def clickUserName(self):
        self.elementClick(self._username_Field, locatorType="xpath")

    def enterUsername(self, username):
        self.sendKeys(username, self._username_Field, locatorType="xpath")
        
    def clickPassWord(self):
        self.elementClick(self._password_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, username="", password=""):
        self.clearFields()
        self.clickUserName()
        #self.clearFields()
        self.enterUsername(username)
        self.clickPassWord()
        #self.clearFields()
        self.clickPassWord()
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//*[contains(text(), 'Dashboard')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Dashboard - Mumbai | MyInstaSafe")

    def logout(self):
        
        #self.nav.navigateToUserSettings()
        time.sleep(3)
        logoutDropDownLinkElement = self.waitForElement(locator=".//a[@class='dropdown-toggle']",
                          locatorType="xpath", pollFrequency=2)
        self.elementClick(element=logoutDropDownLinkElement)
        time.sleep(1)
        logoutLinkElement = self.waitForElement(locator=".//*[@class='list-inline list-unstyled navitem nav navbar-nav']//*[contains(text(),'Sign out')]",
                          locatorType="xpath", pollFrequency=2)

        self.elementClick(element=logoutLinkElement)

    def clearFields(self):
        usernameField = self.getElement(locator=self._username_Field,locatorType="xpath")
        usernameField.clear()
        passwordField = self.getElement(locator=self._password_field,locatorType="xpath")
        passwordField.clear()
