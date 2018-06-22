import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from Common.DriverCreation import DriverStart


class HomePage(DriverStart, unittest.TestCase):


    def enterSearchData(self, driver, searchData):
        driver.find_element_by_name('search').send_keys('iphone')


    def clickSearchButton(self, driver):
        driver.find_element_by_xpath("//div[@id='search']/span/button").click()


if __name__== "__main__":
    unittest.main()
