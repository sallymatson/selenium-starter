from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import path
import re
import os
import pickle

def setup(login_url, target_url, email_element_id, password_element_id, submit_button_id):
    '''
    Using credentials stored in .env OR cookies stashed in cookies.pkl, navigates
    to the desired web page & authenticates.

    Args:
    * login_url: The url of the login page 
    * target_url: The url that follows after successful authentication
    * email_element_id: The HTML element id for the email input box
    * password_element_id: The HTML element id for the password input box
    * submit_button_id: The HTML element id for the login form's submission button
    '''

    driver = webdriver.Chrome()
    driver.get(login_url)
    
    if path.exists('cookies.pkl'):

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)
        driver.get(target_url)

    else:  # No cookies found so must login

        load_dotenv()
        USERNAME = os.environ["USERNAME"]
        PASSWORD = os.environ["PASSWORD"]

        username = driver.find_element_by_id(email_element_id)
        password = driver.find_element_by_id(password_element_id)

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        driver.find_element_by_id(submit_button_id).click()

        pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))

    wait = WebDriverWait(driver, 60)
    wait.until(EC.url_to_be(target_url))

    return(driver)
