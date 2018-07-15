import win32con
import win32gui
import win32ui
import time
import os
from config.config import capture_save_path

# from PIL import Image

def window_capture(filename, box):
    '''
    windows 窗口截图,保存为指定的filename
    无返回值
    '''
    hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    w = box[2] - box[0]
    h = box[3] - box[1]
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    #  参数 (原点)（右下点） mfcDC （左上点）
    saveDC.BitBlt((0,0), (box[2], box[3]), mfcDC, (box[0], box[1]), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

# s1 = time.time()
def capture():
    file_name = os.path.join(capture_save_path, '{}.jpg'.format(int(time.time())))
    # 获取屏幕最大尺寸，即桌面尺寸
    hwnd = win32gui.GetDesktopWindow()
    window_capture(file_name, win32gui.GetWindowPlacement(hwnd)[4])
    time.sleep(1)
    # 用 系统默认 看图软件 打开
    os.system(file_name)
