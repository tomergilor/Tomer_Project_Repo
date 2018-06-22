import unittest
from selenium import webdriver

class DriverStart(unittest.TestCase):

    def setUp(self):
        print "Before test execution"
        self.driver = webdriver.Firefox()
        self.driver.get("http://shop.thetestingworld.com/")
        self.driver.maximize_window()


    def tearDown(self):
        print "After test case execution"
        self.driver.quit()



if __name__== "__main__":
    unittest.main()

