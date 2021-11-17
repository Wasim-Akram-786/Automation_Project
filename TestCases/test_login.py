import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.ReadProperty import ReadConfig
from utilities.Logger import LogGen
class Test_001_Login:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*********************Test Started*************************")
        self.driver=setup
        self.driver.get(self.url)
        actual_title=self.driver.title
        self.driver.close()

        if actual_title == 'Your store. Login':
            assert True
            self.logger.info("*********************Test passed*************************")

        else:
            assert False
            self.logger.error("*********************Test passed*************************")


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()


        if act_title=='Dashboard / nopCommerce administration':
            assert True

        else:
            assert False

