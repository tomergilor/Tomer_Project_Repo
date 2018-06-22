
##### Test cases #####

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from Common.DriverCreation import DriverStart



class Test(unittest.TestCase):

    def setUp(self):
        print "Before test execution"
        self.driver = webdriver.Firefox()
        self.driver.get("https://davidg-mgmt.sentinelone.local")

    def tearDown(self):
        print "After test case execution"
        self.driver.quit()

    def testName(self):
        print "Test case execution"
        time.sleep(3)

        # open the URL (MGMT)
        driver.get('https://davidg-mgmt.sentinelone.local')
        time.sleep(3)
        driver.find_element_by_id('username').send_keys('mgmt')
        time.sleep(3)
        driver.find_element_by_name("password").send_keys('12345678')
        time.sleep(1)
        driver.find_element_by_xpath(
            "//div[@id='content-wrapper']/div/div[2]/div[3]/div/div/form/div[3]/div/ui-checkbox/div/div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()


if __name__== "__main__":
    unittest.main()
