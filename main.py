from selenium import webdriver
import time

url = "https://www.vk.com/"
driver = webdriver.Chrome()
try:
    driver.get(url=url)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
