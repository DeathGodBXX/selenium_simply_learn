from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import timeit
import time


def main():
    browser = webdriver.Chrome()
    browser.get('https://selenium-python-zh.readthedocs.io/en/latest/navigating.html#id9')

    # 浏览历史后退
    browser.back()
    time.sleep(1)

    # 浏览历史前进
    browser.forward()
    time.sleep(1)

    # 利用js打开一个新的窗口
    js = "window.open('https://www.douban.com')"  # 可以看到是打开新的标签页 不是窗口
    browser.execute_script(js)

    # 隐式等待,比time.sleep()智能，告诉WebDriver去等待一定的时间后去查找元素，
    # 只要找到，就继续后续步骤，可以有效防止报错timeoutException
    browser.implicitly_wait(10)

    # 页面截图,虽然页面显示在豆瓣，但是当前窗口还是在selenium，所以截图的是selenium页面
    browser.save_screenshot('selenium-python.png')

    # 跳转到豆瓣页面
    browser.switch_to.window(browser.window_handles[1])

    # 页面滚动到底部
    js = "document.documentElement.scrollTop=8000"
    browser.execute_script(js)
    time.sleep(1)

    # 页面滚动到顶部
    js = "document.documentElement.scrollTop=0"
    browser.execute_script(js)
    time.sleep(1)

    # 浏览器最大化
    browser.maximize_window()

    # 点击电影
    browser.find_element_by_class_name('lnk-movie').click()

    # 跳转到豆瓣电影页面
    browser.switch_to.window(browser.window_handles[2])  # 切换到新打开的豆瓣电影窗口

    # 页面等待，直到‘豆瓣高分’渲染出来，并点击
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='gaia gaia-lite gaia-movie slide-mode']//label[3]"))).click()

    # 页面等待，直到‘更多’按钮渲染，并点击
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='more-link'][contains(@href,'type=movie')]"))).click()

    # 查找p标签下的文本内容并且打印
    i = 1
    while True:
        if i > 20:
            break
        ele = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='list']/a[{i}]")))
        # 页面等待，才不会报错，否则经常报错
        print(ele.text)
        i = i+1
    print('################')

    # 休眠3秒，关闭浏览器
    time.sleep(3)
    browser.quit()


# browser.find_element_by_xpath("//div[@class='gaia gaia-lite gaia-movie slide-mode']//label[3]").click()
# ele = browser.find_element_by_xpath("//a[@class='more-link'][contains(@href,'type=movie')]")
# ele.click()

# ele = browser.find_element_by_xpath("//div[@class='list']//p[@class='']")  # 可能出现网页内容还没渲染出来，就报错。窗口定位错误
# print(ele.text)  # 经常报错，由于网页采用ajax加载技术，有可能网页还没加载出来，就执行上述语句，导致报错，故而采用页面等待来获取内容

if __name__ == '__main__':
    # 重复4次调用1次main()操作流程，并对每次操作流程计时
    ts = timeit.repeat(lambda: main(), number=1, repeat=4)
    print(ts)

