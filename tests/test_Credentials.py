import pytest
from selenium.webdriver.support.select import Select

from TestData.test_HomePageData import TestHomeData
from Utilities.testbaseclass import Test_BaseClass
from testPageObjects.testHomePage import TestHomePage


class TestCredentials(Test_BaseClass):

    def test_formSubmission(self,getdata):
        log = self.getLogger()
        homepage = TestHomePage(self.driver)
        homepage.getname().send_keys(getdata['Firstname'])
        log.info("First Name is: "+getdata['Firstname'] )

        homepage.getemail().send_keys(getdata['Email'])

        homepage.getpassword().send_keys('123456')
        homepage.getchecked().click()


        self.selectoptionbytext(homepage.getgender(),getdata['Gender'])  #used select package for dropdown



        homepage.getdob().send_keys('12-01-1947')

        homepage.getsubmit().click()

        message = homepage.getassertn().text
        assert "Success" in message
        self.driver.refresh()                   #if you have 2 cases on same page


    @pytest.fixture(params=TestHomeData.test_Credentials_Data)
    def getdata(self, request):
        return request.param
