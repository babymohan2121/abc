from selenium.webdriver.common.by import By

class Baseclass:

    @staticmethod
    def enter_URL(driver):
        driver.get("https://www.facebook.com/")

    @staticmethod
    def enter_Username(driver,username):
        driver.find_element(By.ID,'email').send_keys(username)

    @staticmethod
    def enter_Password(driver,password):
        driver.find_element(By.ID,'pass').send_keys(password)

    @staticmethod
    def click_login(driver):
        driver.find_element(By.NAME,'login').submit()
