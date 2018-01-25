import logging
import string
import time

from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from asyncio.tasks import sleep


class ControllerPages(BasePage,SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #Locator
    _whatfix = ".//button[@class='WFSTAY']" 
    _iframe =".//*[@id='wfx-frame-smartPopup']" 
    _controllers_gateways_menu = ".//span[contains(text(),'Controllers &')]"    
    _controller_menu = ".//a[contains(text(),'Controllers')]"
    _add_button = ".//button[contains(text(),'Add')]"   
    _heading_text=".//h2[contains(text(),'Add Controller')]"
    _cloudServer_field = ".//div[@class='selectize-input']"
    _cloudServer_list = ".//div[@role='option']"
    _name_field = ".//*[@id='vpn_name']"    
    _protocol_field = ".//*[@id='protocol']/option"
    _portNumber_field = ".//*[@id='port']"
    _internalNetwork_field = ".//*[@id='network']"
    _netmaskBit_field = ".//div[@name='netmask_bits']/descendant::div[@class='selectize-input']"
    _netmaskBit_list = ".//div[@role='option']"
    _save_button =".//button[@class='theme-sm-btn theme-purple-btn btn-save']"
    _controller_entry = ".//a[contains(text(),'controller')]"
    _close_addwindow = ".//a[@class='close_slide ion-android-close']"
    _checkBox_single = ""
    _checkBox_selectAll = ""
    
            
    def clickAddButton(self):
        self.elementClick(self._add_button, locatorType="xpath")
  
    def verifyAddWindow(self):
        heading = self.isElementPresent(self._heading_text, locatorType="Xpath")
        self.log.info("Add window appear status is " + str(heading))
        
    def selectCloudServerDropDown(self, cloudServer):
        self.elementClick( self._cloudServer_field, locatorType="xpath")
        self.singleSelect_set_selections( self._cloudServer_list, locatorType="xpath",searchfor=cloudServer )
        
    def enterControllerName(self, controller):
        self.sendKeys(controller, self._name_field, locatorType="xpath", element="controller name")
        
    def selectProtocol(self, protocol):
        self.singleSelect_set_selections(self._protocol_field, locatorType="xpath", searchfor=protocol)
     
    def enterPortNumber(self, port):
        self.sendKeys(port, self._portNumber_field, locatorType="xpath")
     
    def enterInternalNetwork(self, ip):
        self.sendKeys(ip, self._internalNetwork_field, locatorType="xpath")
     
    def enterNetmaskBit(self, netmaskBit):
        self.elementClick( self._netmaskBit_field, locatorType="xpath")
        self.singleSelect_set_selections(self._netmaskBit_list, locatorType="xpath", searchfor=netmaskBit)
        
    def clickSaveButton(self):
        self.elementClick(locator =self._save_button, locatorType="Xpath")    

    def closeAddWindow(self):
        self.elementClick(locator= self._close_addwindow, locatorType="Xpath", element="closeAddWindow")
            
    def verifyAddController(self, name):
        controller_entry = self._controller_entry.replace("controller", name)
        self.log.info(controller_entry)
        self.waitForElement(locator= controller_entry, locatorType="Xpath", timeout=30, pollFrequency=1)
        return self.isElementPresent(locator= controller_entry, locatorType="Xpath", element= "none")
        
    def clearFields(self):
        portNumberField = self.getElement(locator=self._portNumber_field,locatorType="xpath")
        portNumberField.clear()
    
    def checkbox(self):
        self.elementClick(locator="", locatorType="Xpath", element="checkBox")
 
 ##--------------------------------------------------------------------------------------------------------------------##
 
 
 
 
    def close_Whatfix_Windows(self):
        self.log.info("waiting for the element")
        time.sleep(10)
        self.switch_to(locator=self._iframe,locatorType="Xpath")
        self.log.info("switching frame now")        
        self.elementClick(locator=self._whatfix, locatorType="Xpath", element="whatfix")
        self.switch_to_default()

    def navigateControllerPage(self):
        self.waitForElement(self._controllers_gateways_menu, locatorType="Xpath", pollFrequency=1) 
        self.elementClick(self._controllers_gateways_menu, locatorType="Xpath")
        self.waitForElement(self._controller_menu, locatorType="Xpath", pollFrequency=1)         
        self.elementClick(self._controller_menu, locatorType="Xpath")
        #self.verifyPageTitle(self, "titleToVerify")

    def navigate_to_Controller_Add_window(self):    
        self.navigateControllerPage()
        self.clickAddButton()
        self.verifyAddWindow()           

       
    def add_Single_Controller(self, cloudServer="", controllerName="", protocol="", port ="", internalNetwork="", netmaskBit="" ):    
        time.sleep(2)
        self.clearFields()
        self.selectCloudServerDropDown(cloudServer)
        self.enterControllerName(controllerName)
        self.selectProtocol(protocol)
        self.enterPortNumber(port)
        self.enterInternalNetwork(internalNetwork)
        self.enterNetmaskBit(netmaskBit)
        self.clickSaveButton()
        self.closeAddWindow()
        
        
    def addMultipleController(self,cloudServer, name, protocol, port, internalNetwork, netmaskBits):
        self.selectCloudServerDropDown(cloudServer)
        self.enterControllerName(name)
        self.selectProtocol(protocol)
        self.enterPortNumber(port)
        self.enterInternalNetwork(internalNetwork)
        self.enterNetmaskBit(netmaskBits)
        self.clickSaveButton()
                       
        
  #  def deleteSigleController(self,):
      #  self.
        
 #   def deleteMultipaleController(self,):
        
        
          #  def deleteAll Controller(self):
            



   # def single_Delete(self):
