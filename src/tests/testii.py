'''
Created on 01-Jan-2018

@author: user
'''
import logging
import unittest
import pytest
import utilities.custom_logger as cl
from pages.companyPortal.controller_Page import ControllerPages
from utilities.read_data import getCSVData
from utilities.teststatus import Status
from ddt import ddt, data, unpack

#from pages.companyPortal.controller_Page import ControllerPage
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ControllerTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = ControllerPages(self.driver)
        self.ts = Status(self.driver)
       
    @pytest.mark.run(order=2)
    def test_t1AddController(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1Addcontroller start")
        self.log.info("*#" * 20)
        self.cp.addController("isademo", "test", "TCP", "1214", "10.12.14.0", "27")
        result = self.cp.verifyAddController("test")
        assert result == True
    @pytest.mark.run(order=1)
    def open_add_window(self):
        self.log.info("test_open_add_window")
        self.cp.open_add_windows()
