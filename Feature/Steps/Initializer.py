from selenium import webdriver


class Baseclass:
    driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\chromedriver_92\\chromedriver.exe")

    @staticmethod
    def load_browser():
        Baseclass.driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\chromedriver_92\\chromedriver.exe")
        Baseclass.driver.maximize_window()
        Baseclass.driver.implicitly_wait(10)

