from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = Chrome()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)  # 跟time.sleep类似，比time.sleep更加智能，不会被动的等待时间结束
wait = WebDriverWait(driver, 10)  # 等待时间
ele = wait.until(EC.presence_of_element_located((By.ID, "kw")))
ele.send_keys("数学")
wait = WebDriverWait(driver, 10)
ele = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
ele.click()
driver.get('https://docs.python.org/3/library/multiprocessing.html')
driver.get('https://blog.csdn.net/DarrenXf/article/details/82110962')

i = 1
while i <= 5:
    time.sleep(1)
    driver.back()  # 后退
    driver.forward()  # 前进
    i = i + 1
