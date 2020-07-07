from selenium.webdriver.common.by import By

class TestConfirm:
    def __init__(self, driver):
        self.driver = driver


    #self.driver.find_element_by_link_text('India')
    country = (By.LINK_TEXT,"Austria")
    def testgetcountry(self):
        return self.driver.find_element(*TestConfirm.country)

    value = (By.ID,"country")
    def testgetvalue(self):
        return self.driver.find_element(*TestConfirm.value)

    # driver.find_element_by_xpath("//label[contains(text(),'I agree with the')]")
    tnc = (By.XPATH,"//label[contains(text(),'I agree with the')]")
    def testgettnc(self):
        return self.driver.find_element(*TestConfirm.tnc)

    # self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
    buy = (By.XPATH,"//input[@class='btn btn-success btn-lg']")
    def testgetpurchased(self):
        return self.driver.find_element(*TestConfirm.buy)

    # self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)
    note = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
    def testgetnote(self):
        return self.driver.find_element(*TestConfirm.note)


    ## assert 'Success' in self.driver.find_element_by_xpath("//strong[contains(text(),'Success!')]").text
    checkup = (By.XPATH,"//strong[contains(text(),'Success!')]")
    def testgetchckup(self):
        return self.driver.find_element(*TestConfirm.checkup)