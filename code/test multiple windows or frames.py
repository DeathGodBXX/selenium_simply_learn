from selenium.webdriver import Chrome
from concurrent.futures import ThreadPoolExecutor
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Driver(url):
    driver = Chrome()
    driver.get(url)
    current_windows = driver.window_handles
    print(current_windows)


if __name__ == '__main__':
    urls = ['https://docs.python.org/3/library/multiprocessing.html',
            'https://blog.csdn.net/DarrenXf/article/details/82110962',
            'https://www.json.cn/']
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(Driver, [url for url in urls])
        time.sleep(20)

