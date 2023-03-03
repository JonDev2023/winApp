import ctypes
from ctypes import wintypes

def info(text):
    print('INFO: ' + text)

def waring(text):
    print('WARING: ' + text)

def error(text, error):
    err = error.__init__('ERROR: ' + text)
    raise err

WM_DESTROY = 0x0002

# Definindo Informações
class WINDOWINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("rcWindow", wintypes.RECT),
        ("rcClient", wintypes.RECT),
        ("dwStyle", ctypes.c_uint),
        ("dwExStyle", ctypes.c_uint),
        ("dwWindowStatus", ctypes.c_uint),
        ("cxWindowBorders", ctypes.c_uint),
        ("cyWindowBorders", ctypes.c_uint),
        ("atomWindowType", wintypes.ATOM),
        ("wCreatorVersion", ctypes.c_ushort)
    ]

# Definindo variaveis
excep
user32 = ctypes.windll.user32

def wndProc(hWnd, message, wParam, lParam):
    if message == WM_DESTROY:
        user32.PostQuitMessage(0)
        return 0
    return user32.DefWindowProcW(hWnd, message, wParam, lParam)

def msgBox(message, title, hwnd=None, uType=0):
    user32.MessageBoxW(hwnd, message, title, uType)

class Window:
    def __init__(self, title='', width=800, height=600, win_style=0x00C00000):
        self.title = title
        self.width = width
        self.height = height
        self.win_width = user32.GetSystemMetrics(0)
        self.win_height = user32.GetSystemMetrics(1)
        self.x = int((self.win_width - self.width) / 2)
        self.y = int((self.win_height - self.height) / 2)
        self.win_style = win_style

    def createWindow(self):
        self.hwnd = user32.CreateWindowExW(0, 'STATIC', self.title, self.win_style,
                                           self.x, self.y, self.width, self.height,
                                           None, None, None, None)

    def showWindow(self):
        user32.ShowWindow(self.hwnd, 1)

    def msg_loop(self):
        self.msg = ctypes.wintypes.MSG()
        while user32.GetMessageW(ctypes.byref(self.msg), None, 0, 0) != 0:
            user32.TranslateMessage(ctypes.byref(self.msg))
            user32.DispatchMessageW(ctypes.byref(self.msg))

    def run(self):
        self.showWindow()
        self.msg_loop()