from selenium.webdriver.common.by import By

from testPageObjects.testConfirmtnPage import TestConfirm


class TestCheckout:
    def __init__(self, driver):
        self.driver = driver


    cardTitles= (By.CSS_SELECTOR, ".card-title a")
    def testgetcardtitles(self):
        return self.driver.find_elements(*TestCheckout.cardTitles)

    selection = (By.CSS_SELECTOR,".card-footer button")
    def testselectitem(self):
        return self.driver.find_elements(*TestCheckout.selection)

    outbtn = (By.XPATH,"//button[@class='btn btn-success']")
    def testgetout(self):
        self.driver.find_element(*TestCheckout.outbtn).click()
        Country  = TestConfirm(self.driver)
        return Country

    # self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
    finalout = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    def testfinalout(self):
        return self.driver.find_element(*TestCheckout.finalout)
