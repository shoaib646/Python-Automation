import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.testbaseclass import Test_BaseClass
from testPageObjects.testCheckoutPage import TestCheckout
from testPageObjects.testConfirmtnPage import TestConfirm
from testPageObjects.testHomePage import TestHomePage


class TestOne(Test_BaseClass):
    def test_e2e(self):
        log = self.getLogger()


        homepage = TestHomePage(self.driver)
        CardTitles = homepage.testshopbtn()
        log.info("Getting all product titles")
        self.driver.execute_script("window.document.body.scrollTop;")

        cards = CardTitles.testgetcardtitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == 'Blackberry':
                CardTitles.testselectitem()[i].click()

        self.driver.execute_script("window.scrollTo(0,0);")
        CardTitles.testfinalout().click()

        Country = CardTitles.testgetout()
        time.sleep(1)

        self.driver.find_element_by_id("country").send_keys("aus")
        self.verifyLinkPresence("Austria")
        #wait = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, "Austria")))
        Country.testgetcountry().click()

        county = Country.testgetvalue().get_attribute("value")
        log.info(f'Product Purchased : {cardText}')
        log.info(f'Product Purchased From: {county}')
        Country.testgettnc().click()
        Country.testgetpurchased().click()

        print(f'Note:↓ ', Country.testgetnote().text)
        assert 'Success' in Country.testgetchckup().text
        log.info("Purchased done is "+Country.testgetchckup().text+"full")





