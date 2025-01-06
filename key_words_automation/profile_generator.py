from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled") # Reduces bot detection

# Funções somente para salvar e carregar os cookies
def save_cookies(driver, filename):
    with open(filename, "w") as file:
        json.dump(driver.get_cookies(), file)

def load_cookies(driver, filename):
    with open(filename, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

# Função para automatizar o login no Google
def google_login_and_consume_content():
    driver = webdriver.Chrome(options=options)
    driver.get("https://accounts.google.com/signup")

    # Input user data - account creation steps would go here
    # After creation, save cookies for persistent login
    save_cookies(driver, "cookies.json")

    # Simulate content consumption
    driver.get("https://www.google.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Your Topic of Interest")
    search_box.submit()
    time.sleep(2)
    
    # Simulate scrolling and clicking on links
    driver.find_elements(By.CSS_SELECTOR, "h3")[0].click()
    time.sleep(5)  # mimic reading time

    # Store final cookies and session data
    save_cookies(driver, "cookies.json")
    driver.quit()

# Call the function
google_login_and_consume_content()