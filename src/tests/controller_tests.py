import logging
import unittest

from ddt import ddt, data, unpack
import pytest

import utilities.custom_logger as cl
from utilities.read_data import getCSVData
from utilities.teststatus import Status
from pages.companyPortal.controller_Page import ControllerPages
#from pages.companyPortal.controller_Page import ControllerPage
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ControllerTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = ControllerPages(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order = 0)
    def test_close_whatfix_window(self): 
        self.log.info("try to close whatfix_window")
        self.cp.close_Whatfix_Windows()
        self.log.info("close_whatfix_window") 
        
    @pytest.mark.run(after = "test_close_whatfix_windows")
    def test_open_add_window(self):
        self.log.info("test_open_add_window")
        self.cp.navigate_to_Controller_Add_window()              
       
   # @pytest.mark.run()
    def test_t1AddController(self, after = 'test_open_add_window'):
        self.log.info("*#" * 20)
        self.log.info("test_t1Addcontroller start")
        self.log.info("*#" * 20)
        self.cp.add_Single_Controller("isademo", "test", "TCP", "1214", "10.12.14.0", "27")
        result = self.cp.verifyAddController("test")
        assert result == True
        

    @pytest.mark.run(after='test_open_add_window')  
    @data(*getCSVData("C:/Users/user/workspace/com.instasafev2/usource/controllerlist.csv"))
    @unpack
    def test_AddMultipleControllers(self, cloudServer, name, protocol, port, internalNetwork, netmaskBits):
        self.log.info("*#" * 20)
        self.log.info("test_AddMultiplecontroller start")
        self.log.info("*#" * 20)
        self.cp.addMultipleController(cloudServer, name, protocol, port, internalNetwork, netmaskBits)
        result = self.cp.verifyAddController("test")            