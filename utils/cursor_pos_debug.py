import pyautogui

def get_cursor_position_debug () -> None:
    x, y = pyautogui.position()
    print(f"Cursor position: x={x}, y={y}")