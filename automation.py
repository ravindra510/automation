import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# service_obj = Service("/home/osian12/Downloads/chromedriver_122")
driver = webdriver.Chrome(  )
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div ")
count  = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()
    
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"promoinfo")))
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"promoinfo")))