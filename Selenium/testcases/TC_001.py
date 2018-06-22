import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from Common.DriverCreation import DriverStart
from Pages.Home import HomePage

class Test(DriverStart, unittest.TestCase):

    def testName(self):
        home = HomePage()
        home.enterSearchData(self.driver, "iphone")
        home.clickSearchButton(self.driver)


        # print "Test case execution"
        # time.sleep(2)               # wait 2 sec.
        # self.driver.find_element_by_name('search').send_keys('iphone')
        # time.sleep(2)
        #  time.sleep(2)
        # self.driver.find_element_by_xpath("//span[text()='Add to Cart']").click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//span[text()='Checkout']").click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//input[@value='guest']").click()
        # self.driver.implicitly_wait(10)                                     #    wait 10 sec. to the element
        # self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        # time.sleep(2)
        #
        # sel = Select(self.driver.find_element_by_id("input-payment-country"))
        # time.sleep(2)
        # sel.select_by_visible_text("India")
        # time.sleep(2)


if __name__== "__main__":
    unittest.main()
