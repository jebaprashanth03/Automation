# import test_case
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path="local_web_driver\\chromedriver.exe")
# driver.implicitly_wait(30)
driver.maximize_window()




driver.get("http://transport-hub-qa-release.com.s3-website.ap-south-1.amazonaws.com/")
mail_input = driver.find_element(By.XPATH, "//*[@id='email']")
password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
button = driver.find_element(By.XPATH, '//*[@id="mui-1"]')
mail_input.send_keys('admin@gmail.com')
password_input.send_keys('admin')
button.click()

wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/button'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div[2]/button'))).click()
