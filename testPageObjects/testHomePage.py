from selenium.webdriver.common.by import By

from testPageObjects.testCheckoutPage import TestCheckout


class TestHomePage:



    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    def testshopbtn(self):
        self.driver.find_element(*TestHomePage.shop).click()
        CardTitles = TestCheckout(self.driver)
        return CardTitles

    # driver.find_element_by_name("name")
    name = (By.NAME,"name")
    def getname(self):
        return self.driver.find_element(*TestHomePage.name)

    # driver.find_element_by_name("email")
    email = (By.NAME,"email")
    def getemail(self):
        return self.driver.find_element(*TestHomePage.email)

    # driver.find_element_by_id('exampleInputPassword1')
    password = (By.ID,"exampleInputPassword1")
    def getpassword(self):
        return self.driver.find_element(*TestHomePage.password)

    # driver.find_element_by_id("exampleCheck1").click()
    checkbox = (By.ID,"exampleCheck1")
    def getchecked(self):
        return self.driver.find_element(*TestHomePage.checkbox)

    # driver.find_element_by_id('exampleFormControlSelect1')
    gender = (By.ID,"exampleFormControlSelect1")
    def getgender(self):
        return self.driver.find_element(*TestHomePage.gender)

    # driver.find_elements_by_xpath("//input[@type='radio']")
    radio = (By.XPATH,"//input[@type='radio']")
    def getradio(self):
        return self.driver.find_element(*TestHomePage.radio)

    # driver.find_element_by_name("bday")
    dob =  (By.NAME,"bday")
    def getdob(self):
        return self.driver.find_element(*TestHomePage.dob)

    # driver.find_element_by_xpath("//input[@type='submit']")
    submit = (By.XPATH, "//input[@type='submit']")
    def getsubmit(self):
        return self.driver.find_element(*TestHomePage.submit)

    # driver.find_element_by_class_name("alert-success")
    assertn = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
    def getassertn(self):
        return self.driver.find_element(*TestHomePage.assertn)