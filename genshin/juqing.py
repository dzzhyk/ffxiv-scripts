import pyautogui as pg
import win32gui as wgui
import win32con as wcon
import time
from pynput import keyboard
from multiprocessing import Process, Event

window_class = "UnityWndClass"
window_name = u"原神"


def left_click(btn='left'):
    pg.mouseDown(button=btn)
    time.sleep(0.3)
    pg.mouseUp(button=btn)


def my_key(k):
    pg.keyDown(k)
    pg.keyUp(k)


class ListenStartProcess(Process):

    def __init__(self, listen_lock):
        super().__init__()
        self.lock = listen_lock

    def on_press(self, key):
        if key == keyboard.Key.f11:
            print('开始点击')
            self.lock.clear()
            while not self.lock.is_set():
                left_click()
                msg = None
                try:
                    msg = pg.locateOnWindow("genshin/msg.png", window_name, confidence=0.8)
                except Exception:
                    pass
                finally:
                    if msg is not None:
                        pg.moveTo(msg, duration=0.3)
                        left_click()
                self.lock.wait(timeout=0.7)

    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


class ListenStopProcess(Process):

    def __init__(self, listen_lock):
        super().__init__()
        self.lock = listen_lock

    def on_press(self, key):
        if key == keyboard.Key.f12:
            print('终止点击')
            self.lock.set()

    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    listen_lock = Event()
    hwnd = wgui.FindWindow(window_class, window_name)
    print("Window `{0}` handle: 0x{1:016X}".format(window_name, hwnd))
    if hwnd != 0:
        if wgui.IsIconic(hwnd):
            wgui.ShowWindow(hwnd, wcon.SW_SHOWNORMAL)
        else:
            wgui.ShowWindow(hwnd, wcon.SW_SHOWNORMAL)
    wgui.SetForegroundWindow(hwnd)

    p1 = ListenStartProcess(listen_lock)
    p1.start()
    p2 = ListenStopProcess(listen_lock)
    p2.start()

    p1.join()
    p2.join()
