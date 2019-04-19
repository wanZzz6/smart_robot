import time
from selenium import webdriver
from selenium.webdriver.remote.errorhandler import WebDriverException

driver = ''


def startChrom():
    try:
        driver = webdriver.Chrome()
        # 设置Chrom浏览器窗口位置
        driver.set_window_rect(x=812, y=0, width=731, height=831)
        time.sleep(1)
        return driver
    except Exception as e:
        print('谷歌启动失败!', e)


def search_kw(keyword):
    global driver
    if not driver.__class__.__name__ == 'WebDriver':
        driver = startChrom()
        if not driver:
            return
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd={}'.format(keyword)
    try:
        driver.get(url)
    except WebDriverException as e:
        driver = startChrom()
        driver.get(url)
        return 'ok'
