from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ertech.id/followers-instagram-gratis/")

username = driver.find_element(By.ID, value="username_ig")
username.send_keys("sunwukong0909")

password = driver.find_element(By.ID, value="password_ig")
password.send_keys("AkuTestingPython")

login_button = driver.find_element(By.ID, value="ig_login_btn")
login_button.click()


# driver.quit()