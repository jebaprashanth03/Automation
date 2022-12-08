# import test_case
import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path="local_web_driver\\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
# driver.get("http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/")

def open_th_web():
    driver.get("http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/")

def th_login(mail_id, password):
    mail_input = driver.find_element(By.XPATH, "//*[@id='email']")
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    button = driver.find_element(By.XPATH, '//*[@id="mui-1"]')

    mail_input.send_keys(mail_id)
    password_input.send_keys(password)
    button.click()
    time.sleep(2)


def logout():
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/button').click()


def test_login_excel(mail_id, password):
    open_th_web()
    th_login(mail_id, password)
    if driver.current_url == 'http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/':
        return False
    elif driver.current_url == 'http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/dashboard':
        logout()
        return True

def write_excel():
    login_test = pd.read_excel("test_case_excel\\login_test_cases.xlsx")
    for index, row in login_test.iterrows():
        if bool(row['expected_login']) == test_login_excel(row['email'], row['password']):
            login_test.loc[index, "pass_or_fail"] = 'Pass'
        else:
            login_test.loc[index, "pass_or_fail"] = 'Fail'

    login_test.to_excel('test_case_excel\\login_test_cases_results.xlsx')
    driver.close()

write_excel()
