from selenium import webdriver
from selenium.webdriver.remote.errorhandler import WebDriverException
import time

driver = ''


def startChrom():
    """启动谷歌驱动"""
    try:
        # 如果为将谷歌驱动添加环境变量，则需要指明启动路径：
        # driver = webdriver.Chrome(executable_path='../chromedriver.exe')

        driver = webdriver.Chrome()
        # chrom浏览器窗口位置
        driver.set_window_rect(x=812, y=0, width=731, height=831)
        time.sleep(1)
        return driver
    except Exception as e:
        print('谷歌启动失败!', e)


def search_kw(keyword):
    """百度搜索"""
    global driver
    if not driver.__class__.__name__ == 'WebDriver':
        driver = startChrom()
        if not driver:
            return
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd={}'.format(keyword)
    try:
        driver.get(url)
    except WebDriverException:
        driver = startChrom()
        driver.get(url)
        return 'ok'
