from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Test Case: Users can navigate to SignIn page (Target)
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)


# 1. Open page
driver.get("https://www.target.com/")
sleep(2)

# 2. Click Account button
driver.find_element(By.XPATH, "//*[text()='Account']").click()
sleep(2)

# 4. Verify SignIn page opened
header = driver.find_element(By.XPATH, "//*[text()='Sign in' or text()='create']")
print("Sign in text visible:", header.text)

# 3. Click SignIn button from side navigation
driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[2]/ul/div/button").click()
sleep(2)


# SignIn button is shown

driver.find_element(By.XPATH, "//button[text()='Continue']")
print("Sign-in button found")

driver.quit()




