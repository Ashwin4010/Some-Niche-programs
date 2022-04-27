import time
import pyautogui
import tkinter as tk


def screenshot():
    name = int(round(time.time())*1000)
    name = f"C:/Users/Aravind/Desktop/Ashwin/Random Programs/Screenshot Program/screenshots/{name}.png"
    # time.sleep()
    img = pyautogui.screenshot(name)
    img.show()


window = tk.Tk()
window.title("Screenshot GUI")
window.config(padx=30,pady=30)
root = tk.Frame(window)
root.pack()

screenshot = tk.Button(
    window,
    text="Screenshot",
    command=screenshot
)
screenshot.pack(side=tk.LEFT)

close = tk.Button(
    window,
    text="Close",
    command=quit
)
close.pack(side=tk.RIGHT)

root.mainloop()