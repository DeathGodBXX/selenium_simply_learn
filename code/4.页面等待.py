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
# selenium切换窗口

driver.get('https://docs.python.org/3/library/multiprocessing.html')
driver.get('https://blog.csdn.net/DarrenXf/article/details/82110962')

# 1. 获取当前所有的窗口
current_windows = driver.window_handles
print(current_windows)
# 2. 根据窗口索引进行切换
# driver.switch_to.window(current_windows[1])

#  selenium切换iframe
# driver.switch_to.frame("iframe的id")

# 切换进入alert
# alert = driver.switch_to.alert()
# i = 1
# while i <= 5:
#     driver.back()  # 后退
#     driver.forward()  # 前进
#     i = i + 1

# selenium的优缺点
# selenium能够执行页面上的js，对于js渲染的数据和模拟登陆处理起来非常容易
# selenium由于在获取页面的过程中会发送很多请求，所以效率非常低，所以在很多时候需要酌情使用
