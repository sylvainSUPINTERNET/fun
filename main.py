from pywinauto.application import Application
import psutil
from constants.constants import PROCESS_GAME_TITLE
import pyautogui
import win32api
import win32gui
import win32con
import time

pid_minecraft = None


def boot():
    
    # find javaw.exe PID ( minecraft executable NOT the launcher !)
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info["name"] == PROCESS_GAME_TITLE:
            pid_minecraft = proc.pid
        
    # main dim 
    screen_dim = pyautogui.size();
    
    app = Application(backend='win32').connect(process=pid_minecraft)
    app.top_window().set_focus()
    
    # Game window dimensions
    hwnd = app.top_window().handle
    window_pos_left = 0
    windows_pos_top = 0
    windows_pos_width = screen_dim.width
    windows_pos_height = screen_dim.height
    # Move the game window to the specified position
    win32gui.SetWindowPos(hwnd, None, window_pos_left, windows_pos_top, windows_pos_width, windows_pos_height, win32con.SWP_SHOWWINDOW)
    # Get the new window position and size
    placement = win32gui.GetWindowPlacement(hwnd)   
    left, top, right, bottom = placement[4]
    width = right - left
    height = bottom - top
    
    
    # Move to "play" button and the select the first game
    pyautogui.moveTo(width/2, height/2.1) # duration=1
    pyautogui.click()
    pyautogui.moveTo(width/4, height/3.2) # duration=1
    pyautogui.click()
    
    
def in_game():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info["name"] == PROCESS_GAME_TITLE:
            pid_minecraft = proc.pid
    screen_dim = pyautogui.size();
    
    app = Application(backend='win32').connect(process=pid_minecraft)
    app.top_window().set_focus()
    pyautogui.press('esc')
    pyautogui.press('z')
    pyautogui.keyDown('z')
    time.sleep(2)
    pyautogui.keyUp('z')
    
    
    left = 100
    top = 100
    width = 200
    height = 100

    hwnd = app.top_window().handle
    # Draw a red square over the specified area of the game window
    hdc = win32gui.GetDC(hwnd)
    pen = win32gui.CreatePen(win32con.PS_SOLID, 10, win32api.RGB(255, 0, 0))
    brush = win32gui.GetStockObject(win32con.NULL_BRUSH)
    old_pen = win32gui.SelectObject(hdc, pen)
    old_brush = win32gui.SelectObject(hdc, brush)
    win32gui.Rectangle(hdc, left, top, left + width, top + height)
    win32gui.SelectObject(hdc, old_pen)
    win32gui.SelectObject(hdc, old_brush)
    win32gui.ReleaseDC(hwnd, hdc)

    pass



    
if __name__ == '__main__':
    #boot()
    in_game()
    
