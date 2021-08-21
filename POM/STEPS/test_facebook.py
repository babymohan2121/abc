import time

from selenium import webdriver

from POM.PAGES.pages import Baseclass


class Test_Facebook:
    def test_facebook(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\chromedriver_92\\chromedriver.exe")
        driver.maximize_window()

        Baseclass.enter_URL(driver)
        Baseclass.enter_Username(driver,"mohanjayavelmasc2016@gmail.com")
        Baseclass.enter_Password(driver,"7010134741")
        Baseclass.click_login(driver)

        time.sleep(30)


a=Test_Facebook()
a.test_facebook()

