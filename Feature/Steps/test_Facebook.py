from behave import Given , When, Then
from selenium.webdriver.common.by import By

from Feature.Steps.Initializer import Baseclass


@Given ('open browser as "{BROWSER}"')
def openBrowser(context,BROWSER):
    print("browser is opened successfully",BROWSER)
    Baseclass.load_browser()

@When ('enter facebook url as "{URL}"')
def enterURl(context,URL):
    Baseclass.driver.get(URL)

@When ('When enter username as "{USERNAME}"')
def enterusername(context,USERNAME):
    Baseclass.driver.find_element(By.ID,'email').send_keys(USERNAME)

@When ('When enter password as "{PASSWORD}"')
def enterpassword(context,PASSWORD):
    Baseclass.driver.find_element(By.ID,'pass').send_keys(PASSWORD)

@When ('When click login button')
def clicklogin(context):
    Baseclass.driver.find_element(By.NAME,'login').submit()

@Then ('verify the user logged successfully')
def verifylogin(context):
    print("user logged in successfully")