# import test_case
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, executable_path="local_web_driver\\chromedriver.exe")
# driver.implicitly_wait(30)

def open_th_web():
    driver.get("http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/")
    driver.maximize_window()

def th_login(mail_id, password):
    mail_input = driver.find_element(By.XPATH, "//*[@id='email']")
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')

    mail_input.send_keys(mail_id)
    password_input.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="mui-1"]').click()
    time.sleep(2)

    if driver.current_url == 'http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/':
        driver.quit()
        return False
    elif driver.current_url == 'http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/dashboard':
        driver.quit()
        return True

def logout():
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/button').click()

def open_liscence():
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[1]/ul[1]/ul/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[1]/ul[1]/ul/div[1]/div/div/div/ul/div[1]/a').click()


def test_login_excel(mail_id, password):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path="local_web_driver\\chromedriver.exe")
    driver.implicitly_wait(30)

    driver.get("http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/")
    driver.maximize_window()

    mail_input = driver.find_element(By.XPATH, "//*[@id='email']")
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')

    mail_input.send_keys(mail_id)
    password_input.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="mui-1"]').click()
    time.sleep(2)

    if driver.current_url == 'http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/':
        driver.close()
        return False
    elif driver.current_url == 'http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/dashboard':
        driver.close()
        return True


import pandas as pd

login_test = pd.read_excel("test_case_excel\\login_test_cases.xlsx")

for index, row in login_test.iterrows():
    if bool(row['expected_login']) == test_login_excel(row['email'], row['password']):
        login_test.loc[index, "pass_or_fail"] = 'Pass'
    else:
        login_test.loc[index, "pass_or_fail"] = 'Fail'

login_test.to_excel('test_case_excel\\login_test_cases.xlsx')
# print(login_test)