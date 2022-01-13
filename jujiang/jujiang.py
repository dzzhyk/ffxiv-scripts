import pyautogui as pg
import win32gui as wgui
import win32con as wcon
import time

window_class = "FFXIVGAME"
window_name = u"最终幻想XIV"
mission_count = 74

def my_click(btn='left'):
    pg.mouseDown(button=btn)
    time.sleep(0.5)
    pg.mouseUp(button=btn)

def my_key(k):
    pg.keyDown(k)
    pg.keyUp(k)

if __name__ == "__main__":
    hwnd = wgui.FindWindow(window_class, window_name)
    print("Window `{0}` handle: 0x{1:016X}".format(window_name, hwnd))
    if hwnd != 0:
        if wgui.IsIconic(hwnd):
            wgui.ShowWindow(hwnd, wcon.SW_SHOWNORMAL)
        else:
            wgui.ShowWindow(hwnd, wcon.SW_SHOWNORMAL)
    wgui.SetForegroundWindow(hwnd)

    for j in range(mission_count):
        npc1 = pg.locateOnWindow("./npc1.png", window_name, confidence=0.9)
        print(npc1)
        pg.moveTo(npc1, duration=0.3)
        time.sleep(0.5)
        my_click('right')
        time.sleep(0.5)
        my_key('num0')
        craft = pg.locateOnWindow("./craft.png", window_name, grayscale=True, confidence=0.8)
        pg.moveTo(craft, duration=0.3)
        time.sleep(0.5)
        my_click()
        time.sleep(0.5)
        level76 = pg.locateOnWindow("./76.png", window_name, grayscale=True)
        pg.moveTo(level76, duration=0.3)
        time.sleep(0.5)
        my_click()
        mission = pg.locateOnWindow("./mission.png", window_name, grayscale=True, confidence=0.9)
        pg.moveTo(mission, duration=0.3)
        time.sleep(0.5)
        my_click()
        time.sleep(0.5)
        my_key('num0')
        time.sleep(0.5)
        my_key('num0')
        time.sleep(0.5)
        my_key('num0')
        time.sleep(0.5)
        my_key('esc')
        time.sleep(0.5)
        my_key('esc')
        time.sleep(3)
        npc2 = pg.locateOnWindow("./npc2.png", window_name, confidence=0.9)
        pg.moveTo(npc2, duration=0.5)
        time.sleep(0.5)
        my_click('right')
        time.sleep(0.5)
        for i in range(27):
            time.sleep(0.2)
            my_key('num0')
        time.sleep(5)