import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import makedirs, popen
from os.path import join, dirname, abspath, exists


# 你的ChromeDriver路径，需要修改
# chrome_driver_path = './chromedriver'
def open_url():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://bing.mcloc.cn'
    driver.get(url)
    # 等待页面加载完成，具体时间视页面复杂度而定
    time.sleep(5)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_pmage-slot-top')))
    print(element)
    time.sleep(5)
    element.click()
    time.sleep(3)
    # 鼠标滚动
    pyautogui.scroll(-1)
    time.sleep(2)
    return driver


def save_pic():
    driver = open_url()
    # 截取图片，并按照时间保存图片
    screenshot = pyautogui.screenshot(region=(290, 210, 1330, 720))
    current_datetime = time.localtime()
    formatted_datetime = time.strftime("%Y%m%d", current_datetime)
    print("格式化日期和时间:", formatted_datetime)
    screenshot_name = formatted_datetime + '.jpg'
    CURRENT_DIR = dirname(abspath(__file__))
    pic_dir = join(CURRENT_DIR, 'pic')
    if not exists(pic_dir):
        makedirs(pic_dir)
    pic_path = join(pic_dir, screenshot_name)
    screenshot.save(pic_path)
    driver.close()


if __name__ == '__main__':
   save_pic()