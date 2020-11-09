from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time


QUERY_STRING = 'selenium python firefox'


current_path = os.getcwd()
print()
print()
print(f'Current directory: {current_path}')

script_path = os.path.dirname(os.path.realpath(__file__))
print(f'Script directory : {script_path}')

if script_path != current_path:
    print('Changing current directory to script directory... ', end='')
    os.chdir(script_path)
    print('Done!\n')

options = Options()
options.headless = True
options.add_argument("--width=1920")
options.add_argument("--height=1080")

print('Initializing Selenium Webdriver... ', end='')
driver = webdriver.Firefox(options=options, executable_path="../drivers/geckodriver")
print('Done!\n')

print('Navigating to duckduckgo.com... ', end='')
driver.get('https://duckduckgo.com/')
print('Done!\n')

print(f'Get window caption: {driver.title}\n')

print(f'Searching "{QUERY_STRING}""... ', end='')
query_input = driver.find_element_by_id('search_form_input_homepage')
query_input.send_keys(QUERY_STRING)

submit_button = driver.find_element_by_id('search_button_homepage')
submit_button.click()
print('Done!\n')

try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'r1-0')))
    file_name = time.strftime("%Y%m%d%H%M%S-firefox.png")
    driver.get_screenshot_as_file(f'../snapshots/{file_name}')
    print(f'Saved image {file_name} to snapshots directory\n')
except TimeoutException:
    print("Loading took too much time!\n")

driver.quit()
print('Closed browser')